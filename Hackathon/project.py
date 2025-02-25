import pandas as pd
import matplotlib.pyplot as plt

# Reading the file
file_path = 'C:\learning\myfolder\RNSIT-SIC-CP\Hackathon\engineeringdata.csv'
df = pd.read_csv(file_path)

# Analyzing the best branch for entrepreneurship
# Considering factors like startups, emerging technologies, and industry collaboration
df["Startup Score"] = df["Startups in the Field"].apply(lambda x: 3 if x == "Many" else 1)
df["Tech Score"] = df["Emerging Technologies"].apply(lambda x: len(x.split(",")))
df["Industry Score"] = df["Industry Collaboration"].apply(lambda x: 3 if x == "Strong" else 1)
df["Entrepreneurship Score"] = df[["Startup Score", "Tech Score", "Industry Score"]].sum(axis=1)
best_entrepreneurship = df.sort_values("Entrepreneurship Score", ascending=False).iloc[0]["Branch Name"]

# Finding the branch with lowest practical exposure despite high demand
# Analyzing practical exposure, job demand, and internship opportunities
demand_dict = {"Very High": 3, "High": 2, "Moderate": 1, "Low": 0, "Very Low": -1}
df["Demand Score"] = df["Current Demand"].apply(lambda x: demand_dict.get(x))
df["Practical Score"] = df["Practical Exposure"].apply(lambda x: 3 if x == "High" else (2 if x == "Medium" else 1))
df["Practical Exposure Score"] = df[["Demand Score", "Internships (%)", "Practical Score"]].sum(axis=1)
exposure_and_demand = df.sort_values("Practical Exposure Score", ascending=True).iloc[0]["Branch Name"]

# Identifying branches with high salaries but high dropout rates
df["Salary-Dropout Score"] = df["Average Salary (INR)"] - df["Dropout Rates (%)"]
salary_and_dropout = df.sort_values("Salary-Dropout Score", ascending=False).iloc[0]["Branch Name"]

# Displaying the results
print("Best Branch for Entrepreneurship:", best_entrepreneurship)
print("Branch with Lowest Practical Exposure Despite High Demand:", exposure_and_demand)
print("Branch with Good Salaries but High Dropout Rate:", salary_and_dropout)

# Bar charts
# Best branch for entrepreneurship
plt.figure(figsize=(10, 5))
plt.bar(df["Branch Name"], df["Entrepreneurship Score"], color='blue')
plt.xlabel("Branch Name")
plt.ylabel("Entrepreneurship Score")
plt.title("Entrepreneurship Potential by Branch")
plt.show()

# Branch with lowest practical exposure despite high demand
plt.figure(figsize=(10, 5))
plt.bar(df["Branch Name"], df["Practical Exposure Score"], color='red')
plt.xlabel("Branch Name")
plt.ylabel("Practical Exposure Score")
plt.title("Practical Exposure vs Demand")
plt.show()

#Branches with high salaries but high dropout rates
plt.figure(figsize=(10, 5))
plt.bar(df["Branch Name"], df["Salary-Dropout Score"], color='green')
plt.xlabel("Branch Name")
plt.ylabel("Salary - Dropout Score")
plt.title("Salary vs Dropout Rate")
plt.show()
