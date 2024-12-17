import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = {
    "Year": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Percentage": [20, 47, 58, 50, 56, 50, 55, 72]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set Seaborn style
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Year", y="Percentage", marker="o", linewidth=2.5)

# Add title and labels
plt.title("AI Usage in Business (2017-2024)\n(According to McKinsey)", fontsize=16, weight="bold")
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage (%)", fontsize=14)

# Customize the y-axis to show percentage
plt.yticks(range(0, 101, 10))

# Save as PNG
plt.savefig("yearly_percentage_trend.png", dpi=300, transparent=True)

# Show the plot
plt.close()