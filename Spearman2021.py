import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_csv('/Users/yanglinglan/Desktop/Correlation 全 - spearman2021.csv')

# Set the width of each bar
bar_width = 0.2

# Set the positions of the bars on the y-axis
positions = range(len(df['VS.summary'].unique()))

# Create a dictionary to map states to their positions
state_positions = {
    'California': [pos - bar_width * 1.5 for pos in positions],
    'Texas': [pos - bar_width * 0.5 for pos in positions],
    'New York': [pos + bar_width * 0.5 for pos in positions],
    'Florida': [pos + bar_width * 1.5 for pos in positions]
}

# Plot the coefficients for each state
for state in df['States'].unique():
    state_df = df[df['States'] == state]
    plt.barh(state_positions[state], state_df['Coefficient'], height=bar_width, label=state)

# Set the y-ticks to the middle of each group of bars
plt.yticks([pos for pos in positions], df['VS.summary'].unique())

# Add labels and title with increased font size
plt.xlabel('Coefficients', fontsize=14)
plt.ylabel('Vaccination Policy', fontsize=14)
#plt.title('Spearman Correlation Coefficients by States in 2021', fontsize=16)

# Add a legend
plt.legend()

# Show the plot
plt.show()
