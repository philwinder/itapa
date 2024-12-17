import json

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read and parse JSON data
with open('cpi.json', 'r') as file:
    data = json.load(file)

# Filter data for UK, USA and Ireland
uk_data = [entry for entry in data if entry['iso3'] == 'GBR']
us_data = [entry for entry in data if entry['iso3'] == 'USA']
ie_data = [entry for entry in data if entry['iso3'] == 'IRL']

# Convert to DataFrames
df_uk = pd.DataFrame(uk_data)
df_us = pd.DataFrame(us_data)
df_ie = pd.DataFrame(ie_data)

# Set style
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12})  # Increase base font size

# Create single plot
plt.figure(figsize=(12, 8))

# Plot all three countries
sns.scatterplot(data=df_uk, x='year', y='score', color='#2E86C1', s=100, 
                label='United Kingdom')
sns.scatterplot(data=df_us, x='year', y='score', color='#E74C3C', s=100, 
                label='United States')
sns.scatterplot(data=df_ie, x='year', y='score', color='#27AE60', s=100, 
                label='Ireland')

# Add error bars for all countries
plt.errorbar(df_uk['year'], df_uk['score'], 
            yerr=df_uk['standardError'].astype(float),
            color='#2E86C1', 
            capsize=5,
            capthick=1,
            linewidth=1,
            linestyle='none')
plt.errorbar(df_us['year'], df_us['score'], 
            yerr=df_us['standardError'].astype(float),
            color='#E74C3C', 
            capsize=5,
            capthick=1,
            linewidth=1,
            linestyle='none')
plt.errorbar(df_ie['year'], df_ie['score'], 
            yerr=df_ie['standardError'].astype(float),
            color='#27AE60', 
            capsize=5,
            capthick=1,
            linewidth=1,
            linestyle='none')

# Add connecting lines for all countries
plt.plot(df_uk['year'], df_uk['score'], color='#2E86C1', alpha=0.5)
plt.plot(df_us['year'], df_us['score'], color='#E74C3C', alpha=0.5)
plt.plot(df_ie['year'], df_ie['score'], color='#27AE60', alpha=0.5)

# Customize plot
plt.title('CPI Comparison\n(2012-2023)', pad=20)
plt.xlabel('Year')
plt.ylabel('CPI Score')
plt.ylim(0, 100)
plt.tick_params(axis='x', rotation=45)
plt.legend()

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('cpi_comparison.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()