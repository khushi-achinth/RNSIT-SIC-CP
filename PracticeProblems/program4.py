import pandas as pd

# Load the dataset
df = pd.read_csv("C:\Files\Book2.csv")

# Display first few rows to understand the structure of the dataset
print(df.head())

# Understanding the dataset: Checking data types and structure
print(df.info())

# Checking for missing values in each column
print(df.isnull().sum())

from sklearn.preprocessing import LabelEncoder

# Encoding categorical variables
df['Brick'] = LabelEncoder().fit_transform(df['Brick'])
df['Neighborhood'] = LabelEncoder().fit_transform(df['Neighborhood'])

# Display the transformed dataset
print(df)

# DATA VISUALIZATION

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# House Price Distribution
# This histogram visualizes the distribution of house prices in the dataset
'''plt.figure(figsize=(8, 5))
sns.histplot(df["Price"], bins=30, kde=True, color="blue")
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()'''

# Feature Correlation Heatmap
# This heatmap shows the correlation between different numerical features to understand their relationships with price
'''plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()'''

# Price vs Square Footage
# Scatter plot to see how house price varies with square footage
'''plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["SqFt"], y=df["Price"], alpha=0.6, color="red")
plt.title("Price vs. Square Footage")
plt.xlabel("Square Footage (SqFt)")
plt.ylabel("Price")
plt.show()'''

# Price vs Number of Bedrooms
# Boxplot to analyze the impact of the number of bedrooms on house price
'''plt.figure(figsize=(10,5))
sns.boxplot(x=df["Bedrooms"], y=df["Price"], palette="coolwarm")
plt.title("Price vs. Number of Bedrooms")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price")
plt.show()'''

# Average House Price by Neighborhood
# Bar plot to analyze the average house price in different neighborhoods
'''plt.figure(figsize=(12, 6))
sns.barplot(x=df["Neighborhood"], y=df["Price"], estimator=np.mean, palette="magma")
plt.xticks(rotation=45)
plt.title("Average House Price by Neighborhood")
plt.xlabel("Neighborhood")
plt.ylabel("Average Price")
plt.show()
'''

# Impact of Brick Houses on Price
# Boxplot to visualize whether houses made of brick influence house prices
plt.figure(figsize=(6, 5))
sns.boxplot(x=df["Brick"], y=df["Price"], palette="coolwarm")
plt.title("Impact of Brick Houses on Price")
plt.xlabel("Brick House (Yes/No)")
plt.ylabel("Price")
plt.show()
