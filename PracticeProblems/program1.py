'''
This analysis provides an in-depth understanding of the performance of IPL players based on various parameters such as runs scored, wickets taken, team performance, and player nationality. The insights gained can help IPL teams and selectors in making informed decisions regarding player selection, team strategies, and talent scouting. 

By leveraging data-driven analytics, franchises can identify key performers, discover underrated talents, and optimize their squad compositions for upcoming seasons. Moreover, this analysis highlights the importance of experienced Indian batsmen for consistency, the contribution of overseas players in bowling, and the potential of uncapped players as promising assets for the future of IPL cricket.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('C:/Files/IPLData.csv')

# Reading the data
print(df)

# Understanding the data structure
print(df.info())  # Provides data types and non-null values
print(df.isnull().sum())  # Check for missing values
print(df.describe())  # Summary statistics for numerical data

# Handling missing values
# Fill missing numerical values with median
df.fillna(df.median(numeric_only=True), inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Verify missing values are handled
print(df.isnull().sum())

# Statistical analysis

# Top five run scorers
# Get top 5 run scorers
top_run_scorers = df[['Player Name', 'Team', 'Runs']].sort_values(by='Runs', ascending=False).head(5)
print(top_run_scorers)

# Plot top 5 run scorers
'''plt.figure(figsize=(8,5))
sns.barplot(data=top_run_scorers, x="Runs", y="Player Name", palette="viridis")
plt.xlabel("Total Runs")
plt.ylabel("Player Name")
plt.title("Top 5 Run Scorers in IPL")
plt.show()'''

# Top five wicket takers
# Get top 5 wicket-takers
top_wicket_takers = df[['Player Name', 'Team', 'Wickets']].sort_values(by='Wickets', ascending=False).head(5)
print(top_wicket_takers)

# Plot top 5 wicket takers
'''plt.figure(figsize=(14,5))
sns.barplot(data=top_wicket_takers, x="Wickets", y="Player Name", palette="coolwarm")
plt.xlabel("Total Wickets")
plt.ylabel("Player Name")
plt.title("Top 5 Wicket-Takers in IPL")
plt.show()'''

# Team-wise performance
# Aggregate team performance
team_performance = df.groupby('Team').agg({'Runs': 'sum', 'Wickets': 'sum'}).reset_index()
print(team_performance)

# Plot team-wise runs
'''plt.figure(figsize=(10,5))
sns.barplot(data=team_performance, x="Runs", y="Team", palette="magma")
plt.xlabel("Total Runs")
plt.ylabel("Team")
plt.title("Total Runs by Each Team")
plt.show()'''

# Plot team-wise wickets
'''plt.figure(figsize=(10,5))
sns.barplot(data=team_performance, x="Wickets", y="Team", palette="Blues_r")
plt.xlabel("Total Wickets")
plt.ylabel("Team")
plt.title("Total Wickets by Each Team")
plt.show()'''

# Indian vs Overseas Players
# Group by nationality
nationality_performance = df.groupby('Nationality').agg({'Runs': 'mean', 'Average': 'mean', 'Wickets': 'mean'}).reset_index()
print(nationality_performance)

# Plot the comparison
'''plt.figure(figsize=(8,5))
sns.barplot(data=nationality_performance.melt(id_vars=["Nationality"]), x="variable", y="value", hue="Nationality", palette="pastel")
plt.xlabel("Metric")
plt.ylabel("Average Value")
plt.title("Comparison of Indian vs Overseas Players")
plt.show()'''

# Capped and uncapped Players
# Group by capped status
capped_performance = df.groupby('Capped').agg({'Runs': 'mean', 'Average': 'mean', 'Wickets': 'mean'}).reset_index()
print(capped_performance)

# Plot the comparison
plt.figure(figsize=(8,5))
sns.barplot(data=capped_performance.melt(id_vars=["Capped"]), x="variable", y="value", hue="Capped", palette="Set2")
plt.xlabel("Metric")
plt.ylabel("Average Value")
plt.title("Capped vs Uncapped Players' Performance")
plt.show()


