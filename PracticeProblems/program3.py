import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('C:\Files\employee.csv')

# Display first few rows of the dataset
print(df.head()) 

# Checking for missing values
print(df.isnull().sum())

# Drop rows where 'Gender' is missing
df = df.dropna(subset=['Gender'])

# Display updated dataset
print(df)

# Re-check missing values
print(df.isnull().sum())

# Drop rows where 'Senior Management' and 'Team' are missing
df = df.dropna(subset=['Senior Management'])
df = df.dropna(subset=['Team'])

# Display updated dataset
print(df)
print(df.isnull().sum())

# Encode categorical variables
label_encoders = {}  # Store encoders for later inverse transformation if needed

for column in ["First Name", "Gender", "Senior Management", "Team"]:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))  # Convert to string before encoding
    label_encoders[column] = le  # Store encoder for future use

# Print the transformed DataFrame
print(df.head())

# Convert float columns to integers for better analysis
for column in df.select_dtypes(include=['float']).columns:
    df[column] = df[column].astype(int)

# Print the transformed DataFrame
print(df)



# Visualization of Salary Distribution per Team
'''plt.figure(figsize=(10, 5))
sns.barplot(x="Team", y="Salary", data=df, palette="viridis")
plt.xlabel("Team")
plt.ylabel("Salary")
plt.title("Salary Distribution per Team")
plt.xticks(rotation=45)
plt.show()'''

# Histogram for Salary Distribution
'''plt.figure(figsize=(8, 5))
sns.histplot(df["Salary"], bins=5, kde=True, color="blue")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.show()'''

# Boxplot of Salary by Gender
'''plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="Salary", data=df, palette="coolwarm")
plt.xlabel("Gender (0 = Female, 1 = Male)")
plt.ylabel("Salary")
plt.title("Salary Distribution by Gender")
plt.show()'''

# Scatter Plot - Salary vs Bonus
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Bonus %", y="Salary", data=df, hue="Gender", palette="Dark2", s=100)
plt.xlabel("Bonus %")
plt.ylabel("Salary")
plt.title("Salary vs Bonus %")
plt.legend(title="Gender", labels=["Female", "Male"])
plt.show()
