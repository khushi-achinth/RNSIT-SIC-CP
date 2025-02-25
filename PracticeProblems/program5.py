import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
# The dataset contains information about various movies, including budget, earnings, genre, and production studio.
df = pd.read_csv('C:\Files\movies.csv')

# Display the first few rows of the dataset
print(df)

# Understanding the structure of the dataset
print(df.info())

# Statistical summary of numerical columns
print(df.describe())

# Checking for missing values
print(df.isnull().sum())

# Handling missing values:
# Replace NaN values with 0 and replace infinite values with 0 to maintain consistency in calculations
df = df.fillna(0).replace([np.inf, -np.inf], 0)

# Convert only float columns to int for better analysis
df[df.select_dtypes(include=['float']).columns] = df.select_dtypes(include=['float']).astype(int)

# Display the cleaned dataset
print(df)

# Re-check for any remaining missing values
print(df.isnull().sum())

# Data Visualization
# The following plots help analyze movie trends and financial performance.

# 1. Histogram: Distribution of World Gross
# This histogram shows the frequency distribution of world gross earnings.
'''sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(df["WorldGross"], bins=20, kde=True, color="blue")
plt.title("Distribution of World Gross", fontsize=14, fontweight='bold')
plt.xlabel("World Gross (in millions)")
plt.ylabel("Frequency")
plt.show()'''

# 2. Bar Chart: Top 10 highest-grossing movies
# This bar chart highlights the top 10 movies that generated the highest world gross revenue.
'''top_movies = df.nlargest(10, "WorldGross")
plt.figure(figsize=(10, 6))
sns.barplot(y=top_movies["Movie"], x=top_movies["WorldGross"], palette="viridis")
plt.title("Top 10 Highest-Grossing Movies", fontsize=14, fontweight='bold')
plt.xlabel("World Gross (in millions)")
plt.ylabel("Movie")
plt.show()'''

# 3. Box Plot: Budget distribution by genre
# This box plot compares the budgets of different genres, highlighting variations and outliers.
'''plt.figure(figsize=(12, 6))
sns.boxplot(x="Budget", y="Genre", data=df, palette="Set2")
plt.title("Budget Distribution by Genre", fontsize=14, fontweight='bold')
plt.xlabel("Budget (in millions)")
plt.ylabel("Genre")
plt.show()'''

# 4. Correlation Heatmap
# The heatmap visualizes correlations between numerical features, helping us understand key relationships.
'''plt.figure(figsize=(12, 6))
corr_matrix = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=14, fontweight='bold')
plt.show()'''

# 5. Horizontal Bar Chart: Lead studios by total world gross
# This chart highlights the most financially successful movie studios based on cumulative world gross.
studio_gross = df.groupby("LeadStudio")["WorldGross"].sum().nlargest(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=studio_gross, y=studio_gross.index, palette="magma")
plt.title("Top 10 Studios by Total World Gross", fontsize=14, fontweight='bold')
plt.xlabel("Total World Gross (in billions)")
plt.ylabel("Lead Studio")
plt.show()