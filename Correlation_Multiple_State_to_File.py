import pandas as pd
from scipy.stats import spearmanr, kendalltau

# Load your data
df = pd.read_csv("selected_data.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

# Renaming columns for convenience
df = df.rename(columns={
    'V1_Vaccine.Prioritisation..summary.': 'V1',
    'V2A_Vaccine.Availability..summary.': 'V2A',
    'V3_Vaccine.Financial.Support..summary.':'V3',
    'V4_Mandatory.Vaccination..summary.':'V4'
})


states = ['Florida', 'New York', 'Texas', 'California']
all_results = []

# Analyzing data for each state
for state in states:
    state_data = df[df['RegionName'] == state].sort_values(by='Date')
    state_data['VaccinationRateChange'] = state_data['PopulationVaccinated'].diff().dropna()

    policy_columns = ['V1', 'V2A', 'V3', 'V4']
    state_results = []

    # Calculating correlations
    for col in policy_columns:
        spearman_corr, spearman_pvalue = spearmanr(state_data['PopulationVaccinated'], state_data[col], nan_policy='omit')
        kendall_corr, kendall_pvalue = kendalltau(state_data['PopulationVaccinated'], state_data[col], nan_policy='omit')

        state_results.append([state, col, 'Spearman', spearman_corr, spearman_pvalue])
        state_results.append([state, col, 'Kendall', kendall_corr, kendall_pvalue])

    all_results.extend(state_results)

# Creating a DataFrame from the results
columns = ['State', 'Policy', 'Correlation Type', 'Correlation Coefficient', 'P-Value']
results_df = pd.DataFrame(all_results, columns=columns)

# Save the DataFrame to an Excel file
results_df.to_excel('vaccination_policy_correlation_total_population_results.xlsx', index=False)
