import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/yanglinglan/Desktop/selected_data.csv")

# Filter for only the four states you're interested in
states = ['California', 'New York', 'Texas', 'Florida']
filtered_df = df[df['RegionName'].isin(states)]

# Keep only the relevant columns
filtered_df = filtered_df[['Date', 'RegionName', 'PopulationVaccinated']]
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%Y%m%d')

# Set the figure size and plot the data for each state
plt.figure(figsize=(10, 6))
for state in states:
    state_df = filtered_df[filtered_df['RegionName'] == state]
    plt.plot(state_df['Date'], state_df['PopulationVaccinated'], label=state)

# Add titles and labels
plt.title('Population Vaccinated Over Time',fontsize=16)
plt.xlabel('Date',fontsize=14)
plt.ylabel('Population Vaccinated (%)',fontsize=14)
plt.legend()

# Show the plot
plt.show()
