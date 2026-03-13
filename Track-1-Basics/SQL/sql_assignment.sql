-- ==========================================
-- SQL Assignment: Startup Funding Analysis
-- Author: Adarsh
-- Database: startup_db
-- ==========================================

USE startup_db;

-- =================================================
-- Q1: How many startups are there in Pune City?
-- =================================================

SELECT COUNT(*) AS pune_startups
FROM startups
WHERE CityLocation LIKE '%Pune%';


-- =================================================
-- Q2: How many startups in Pune got Seed/Angel funding?
-- =================================================

SELECT COUNT(*) AS pune_seed_angel
FROM startups
WHERE CityLocation LIKE '%Pune%'
AND InvestmentType IN ('Seed Funding','Angel Funding');


-- =================================================
-- Q3: Total amount raised by startups in Pune City
-- =================================================

SELECT
SUM(
    CAST(REPLACE(AmountInUSD, ',', '') AS UNSIGNED)
) AS total_pune_funding
FROM startups
WHERE CityLocation LIKE '%Pune%'
AND AmountInUSD IS NOT NULL
AND AmountInUSD NOT IN ('nan','');


-- =================================================
-- Q4: Top 5 Industry Verticals with highest startups
-- =================================================

SELECT
IndustryVertical,
COUNT(*) AS startup_count
FROM startups
WHERE IndustryVertical IS NOT NULL
AND IndustryVertical NOT IN ('nan','')
GROUP BY IndustryVertical
ORDER BY startup_count DESC
LIMIT 5;
-- Q5: Top Investor by Year

SELECT year, InvestorsName, total_investment
FROM (
    SELECT
        YEAR(STR_TO_DATE(Date,'%d/%m/%Y')) AS year,
        TRIM(InvestorsName) AS InvestorsName,
        SUM(CAST(REPLACE(AmountInUSD, ',', '') AS UNSIGNED)) AS total_investment,
        ROW_NUMBER() OVER (
            PARTITION BY YEAR(STR_TO_DATE(Date,'%d/%m/%Y'))
            ORDER BY SUM(CAST(REPLACE(AmountInUSD, ',', '') AS UNSIGNED)) DESC
        ) AS rn
    FROM startups
    WHERE STR_TO_DATE(Date,'%d/%m/%Y') IS NOT NULL
    AND InvestorsName NOT IN ('N/A','Undisclosed','nan','')
    GROUP BY year, InvestorsName
) ranked
WHERE rn = 1
AND year >= 2010
ORDER BY year;


-- BONUS 1: Top startup by funding in each city

SELECT city, StartupName, total_funding
FROM (
    SELECT
        TRIM(CityLocation) AS city,
        StartupName,
        SUM(CAST(REPLACE(AmountInUSD, ',', '') AS UNSIGNED)) AS total_funding,
        ROW_NUMBER() OVER (
            PARTITION BY TRIM(CityLocation)
            ORDER BY SUM(CAST(REPLACE(AmountInUSD, ',', '') AS UNSIGNED)) DESC
        ) AS rn
    FROM startups
    WHERE CityLocation IS NOT NULL
    AND TRIM(CityLocation) NOT IN ('','nan')
    AND AmountInUSD NOT IN ('nan','undisclosed','')
    GROUP BY TRIM(CityLocation), StartupName
) ranked
WHERE rn = 1
ORDER BY city;


-- BONUS 2: SubVertical with highest number of startups

SELECT TRIM(SubVertical) AS SubVertical,
COUNT(*) AS startup_count
FROM startups
WHERE SubVertical IS NOT NULL
AND TRIM(SubVertical) NOT IN ('','nan')
GROUP BY SubVertical
ORDER BY startup_count DESC
LIMIT 1;


-- BONUS 3: SubVertical with highest funding

SELECT TRIM(SubVertical) AS SubVertical,
SUM(CAST(REPLACE(AmountInUSD, ',', '') AS UNSIGNED)) AS total_funding
FROM startups
WHERE SubVertical IS NOT NULL
AND TRIM(SubVertical) NOT IN ('','nan')
GROUP BY SubVertical
ORDER BY total_funding DESC
LIMIT 1;