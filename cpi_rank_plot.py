import json

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read and parse JSON data
with open('cpi.json', 'r') as file:
    data = json.load(file)

# Create a DataFrame with all data
df = pd.DataFrame(data)

# Create a pivot table showing ranks for each country by year
ranks_by_year = pd.pivot_table(
    df,
    values='rank',
    index='year',
    columns='iso3',
    aggfunc='first'
)[['GBR', 'USA', 'IRL']]

# Set style
sns.set_style("whitegrid")

# Create plot with larger figure size to accommodate annotations
plt.figure(figsize=(14, 10))

# Plot rank positions
plt.plot(ranks_by_year.index, ranks_by_year['GBR'], 'o-', color='#2E86C1', label='United Kingdom', linewidth=2)
plt.plot(ranks_by_year.index, ranks_by_year['USA'], 'o-', color='#E74C3C', label='United States', linewidth=2)
plt.plot(ranks_by_year.index, ranks_by_year['IRL'], 'o-', color='#27AE60', label='Ireland', linewidth=2)

# Add annotations for key events
events = {
    2016: ('Brexit\nReferendum', 10),  # Adjust y position as needed
    2017: ('Trump Takes\nOffice', 17.5),
    2020: ('COVID-19\nPandemic', 10)
}

# Add annotations with arrows
for year, (event, y_offset) in events.items():
    plt.annotate(event, 
                xy=(year, ranks_by_year.loc[year].mean()),  # Arrow points to average rank that year
                xytext=(year, y_offset),  # Text position
                ha='center',
                bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'),
                fontsize=10)

# Customize plot
plt.title('CPI Rank Position Over Time with Key Events\n(2012-2023)', pad=20, fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Rank Position\n(Lower is Better)', fontsize=12)

# Invert y-axis since lower rank numbers are better
plt.gca().invert_yaxis()

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Add legend
plt.legend(fontsize=10)

# Adjust layout to prevent annotation cutoff
plt.tight_layout()

# Save the plot
plt.savefig('cpi_rank_comparison.png', dpi=300, bbox_inches='tight')
plt.close() 