import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("energy_consumption_dataset.csv")

# Convert the 'timestamp' column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Remove rows with missing values
df_cleaned = df.dropna()

# Explore the distribution of energy consumption
plt.figure(figsize=(10, 6))
sns.histplot(df["energy_consumption"], kde=True)
plt.title("Energy Consumption Distribution")
plt.xlabel("Energy Consumption")
plt.ylabel("Frequency")
plt.show()

# Plot energy consumption over time for each building
plt.figure(figsize=(14, 8))
sns.lineplot(x="timestamp", y="energy_consumption", hue="building_id", data=df)
plt.title("Energy Consumption Over Time for Each Building")
plt.xlabel("Timestamp")
plt.ylabel("Energy Consumption")
plt.show()

import seaborn as sns

# Extract month and day of week from timestamp
df["month"] = df["timestamp"].dt.month
df["day_of_week"] = df["timestamp"].dt.dayofweek

# Plot average energy consumption by month and day of week
plt.figure(figsize=(16, 6))
plt.subplot(1, 2, 1)
sns.lineplot(x="month", y="energy_consumption", data=df, errorbar=None)
plt.title("Average Energy Consumption by Month")

plt.subplot(1, 2, 2)
sns.lineplot(x="day_of_week", y="energy_consumption", data=df, errorbar=None)
plt.title("Average Energy Consumption by Day of Week")

plt.show()
