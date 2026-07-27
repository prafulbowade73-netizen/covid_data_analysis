import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("covid_data.csv")

# Show first 5 rows
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Statistical Summary
print("\nSummary:")
print(df.describe())

# -----------------------------
# 1. Confirmed Cases Trend
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Confirmed"], marker='o')
plt.title("COVID-19 Confirmed Cases")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------

# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Deaths"], color='red', marker='o')
plt.title("COVID-19 Death Cases")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------

# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(df["Date"], df["Recovered"])
plt.title("Recovered Cases")
plt.xlabel("Date")
plt.ylabel("Recovered")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Active Cases
# -----------------------------
plt.figure(figsize=(10,5))
plt.bar(df["Date"], df["Active"])
plt.title("Active Cases")
plt.xlabel("Date")
plt.ylabel("Active Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
latest = df.iloc[-1]

plt.figure(figsize=(6,6))
plt.pie(
    [latest["Recovered"], latest["Deaths"], latest["Active"]],
    labels=["Recovered", "Deaths", "Active"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("COVID-19 Distribution (Latest Data)")
plt.show()

# -----------------------------
# 6. Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["Confirmed"], df["Deaths"])
plt.title("Confirmed vs Deaths")
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")
plt.grid(True)
plt.show()
