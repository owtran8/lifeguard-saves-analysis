# lifeguard-saves-analysis
SQL and NumPy analysis of lifeguard rescue data with multiple linear regression modeling

Lifeguard Rescue Risk Analysis (SQL + NumPy)
Project Overview:

During Summer 2025 (June – September), I worked as a lifeguard at Calibunga Water Park.

While working there, I monitored swimmers across all attractions, enforced safety rules, and performed both shallow and deep-water rescues when necessary. I also became CPR certified and worked closely with my team to maintain a safe environment for guests.

The dataset used in this project was compiled from official rescue report sheets recorded during shifts. These reports documented:

Number of saves
Time of day
Location of rescue (specific slide or attraction)

This project is based on real operational data collected during my time working at the park.



In this project, I analyzed lifeguard rescue activity from a water park using SQL and Python.

The main objectives were:
Determine which attractions generate the most rescues
Identify when rescues occur most frequently. Build a simplified regression model to measure key risk drivers. The focus was on converting raw operational data into clear, interpretable safety insights.

Tools & Skills Used:
SQL aggregation (GROUP BY, SUM, AVG)
Running SQL inside Python (SQLite)
Linear regression built from scratch using NumPy
Data visualization with Matplotlib
Model evaluation using MSE and R²
Total Rescues by Location
I first used SQL to compute total rescues by attraction.

<img src="images/Total_Saves_by_Location.png" width="700">
Observations:
Shotgun Falls accounts for the highest number of rescues. Rescue activity is not evenly distributed across attractions. Certain areas clearly present higher safety risk.

Average Rescues by Time of Day:
Next, I analyzed rescue frequency across different time blocks.

<img src="images/Avg_Saves_By_Time_Of_Day.png" width="700">
Observations
Rescue frequency peaks in the afternoon. Morning periods show noticeably lower activity. Risk appears to rise as the day progresses.

Simplified Regression Model:

I constructed a focused Multiple Linear Regression model using:

Temperature
Lifeguards_On_Duty
High_Risk_Location
Peak_Time
Estimated model:

Saves = -0.50
(0.0067 × Temperature)
(0.0091 × Lifeguards_On_Duty)
(0.6673 × High_Risk_Location)
(0.2982 × Peak_Time)

What the Model Suggests:

High-risk locations have the strongest effect on rescue frequency. Peak hours meaningfully increase expected rescues. Temperature has a small positive impact Lifeguard count's don't affect the amount of saves. 

Model Performance
MSE ≈ 0.45
R² ≈ 0.19

The model explains about 19% of the variation in rescue counts.

This indicates that while environmental and operational conditions influence rescues, many events are still driven by unpredictable factors.

Model Fit Visualization
<img src="images/Actual_vs_Predicted_Saves.png" width="700">

The spread around the diagonal line reflects the moderate explanatory power of the model.

Why This Matters:

This project demonstrates the ability to:
Extract operational insights using SQL
Build regression models without machine learning libraries
Simplify models for clarity and interpretability
Translate statistical output into practical risk insights

Overall, the analysis highlights how high-risk zones being like Shotgun Falls and peak hours are the primary contributors to how many saves happen. 
