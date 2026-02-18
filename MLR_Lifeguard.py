# LIFEGUARD OPERATIONS ANALYSIS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3


# 1. Load dataset into temporary SQL database

data = pd.read_csv("Calibunga_Final_Dataset.csv")

connection = sqlite3.connect(":memory:")
data.to_sql("park", connection, index=False, if_exists="replace")

print("\nData successfully loaded.\n")


# 2. Where do most rescues happen?

loc_query = """
SELECT Location, SUM(Saves) AS Total_Saves
FROM park
GROUP BY Location
ORDER BY Total_Saves DESC;
"""

location_totals = pd.read_sql(loc_query, connection)

print("Rescues by Location:")
print(location_totals)

plt.figure()
plt.bar(location_totals["Location"], location_totals["Total_Saves"])
plt.title("Total Rescues by Park Area")
plt.xticks(rotation=40)


# 3. When are rescues most common?

time_query = """
SELECT TimeBlock, AVG(Saves) AS Avg_Saves
FROM park
GROUP BY TimeBlock
ORDER BY Avg_Saves DESC;
"""

time_avg = pd.read_sql(time_query, connection)

print("\nAverage Rescues by Time of Day:")
print(time_avg)

plt.figure()
plt.bar(time_avg["TimeBlock"], time_avg["Avg_Saves"])
plt.title("Average Rescues by Time Block")


# 4. Build a focused regression model

model_query = """
SELECT Temperature_F,
       Lifeguards_On_Duty,
       High_Risk_Location,
       Peak_Time,
       Saves
FROM park;
"""

model_data = pd.read_sql(model_query, connection)

features = model_data.drop(columns=["Saves"]).astype(float).values
target = model_data["Saves"].astype(float).values

ones = np.ones((features.shape[0], 1))
X = np.hstack([ones, features])

weights, *_ = np.linalg.lstsq(X, target, rcond=None)

print("\nLinear Model:")
print("---------------------------")

variables = ["Intercept"] + list(model_data.columns[:-1])

equation = f"ŷ = {weights[0]:.4f}"
for i in range(1, len(weights)):
    equation += f" + ({weights[i]:.4f} * {variables[i]})"

print(equation)

print("\nModel Coefficients:")
for i, name in enumerate(variables):
    print(f"{name}: {weights[i]:.4f}")

predictions = X @ weights

mse = np.mean((target - predictions) ** 2)
r2 = 1 - (np.sum((target - predictions) ** 2) /
          np.sum((target - np.mean(target)) ** 2))

print("\nModel Metrics:")
print("MSE:", round(mse, 4))
print("R²:", round(r2, 4))


# 5. Visual check of model performance

plt.figure()
plt.scatter(target, predictions, alpha=0.4)
plt.plot([target.min(), target.max()],
         [target.min(), target.max()],
         linestyle="--")

plt.title("Model Fit: Actual vs Predicted Rescues")
plt.xlabel("Actual Rescues")
plt.ylabel("Predicted Rescues")

plt.show()

connection.close()
