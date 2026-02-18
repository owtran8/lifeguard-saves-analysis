-- =========================================
-- LIFEGUARD SAVES BUSINESS ANALYSIS
-- =========================================


-- 1️⃣ Total Saves by Location
-- Business Question:
-- Which attractions require the most safety attention?
-- This shows:
-- Which rides are most dangerous
-- Validates your real-world experience (Shotgun Falls, Activity Pool, Wave Pool)

SELECT 
    Location,
    SUM(Saves) AS Total_Saves
FROM Calibunga_CSV
GROUP BY Location
ORDER BY Total_Saves DESC;



-- 2️⃣ Average Saves by Time of Day
-- Business Question:
-- Are afternoons more dangerous than mornings or lunch?

SELECT 
    TimeBlock,
    AVG(Saves) AS Avg_Saves
FROM Calibunga_CSV
GROUP BY TimeBlock
ORDER BY Avg_Saves DESC;



-- 3️⃣ Impact of Attendance on Saves
-- Business Question:
-- Do higher crowd sizes increase rescue incidents?

SELECT 
    Attendance,
    Saves
FROM Calibunga_CSV;



-- 4️⃣ Hot Days vs Non-Hot Days
-- Business Question:
-- Do hotter temperatures increase rescue frequency?

SELECT 
    Hot_Day,
    AVG(Saves) AS Avg_Saves
FROM Calibunga_CSV
GROUP BY Hot_Day;



-- 5️⃣ Weekend vs Weekday Risk
-- Business Question:
-- Are weekends riskier than weekdays?

SELECT 
    Is_Weekend,
    AVG(Saves) AS Avg_Saves
FROM Calibunga_CSV
GROUP BY Is_Weekend;



-- 6️⃣ High Risk Locations Validation
-- Business Question:
-- Do designated high-risk zones actually produce more saves?

SELECT 
    High_Risk_Location,
    AVG(Saves) AS Avg_Saves
FROM Calibunga_CSV
GROUP BY High_Risk_Location;



-- 7️⃣ Continuous Variables for Regression Modeling
-- This query extracts only the numeric features
-- used later in the NumPy regression model

SELECT
    Attendance,
    Temperature_F,
    High_Risk_Location,
    Peak_Time,
    Is_Weekend,
    Hot_Day,
    Lifeguards_On_Duty,
    Saves
FROM Calibunga_CSV;




-- From three most important SQL findings: 
-- 1. Shotgun Falls and Activity Pool generated the highest total rescue incidents.
-- 2. Afternoon time blocks showed elevated average saves, suggesting fatigue and peak crowd impact.
-- 3. High-attendance days demonstrated increased rescue frequency, validating attendance as a predictive feature.