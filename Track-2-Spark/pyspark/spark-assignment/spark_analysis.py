import os
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, to_date, year

# -------------------------
# 1️⃣ Start Spark
# -------------------------

spark = (
    SparkSession.builder.appName("StartupAnalysis")
    .master("local[*]")
    .config("spark.sql.legacy.timeParserPolicy", "LEGACY")
    .config("spark.jars", "mysql-connector-j-9.6.0.jar")
    .getOrCreate()
)

# -------------------------
# 2️⃣ Load Data
# -------------------------

startup_df = spark.read.csv("data/startup.csv", header=True, inferSchema=True)

consumer_df = spark.read.csv("data/consumerInternet.csv", header=True, inferSchema=True)

# Combine datasets
df = startup_df.unionByName(consumer_df)

# -------------------------
# 3️⃣ Data Cleaning
# -------------------------

df = df.withColumn("Amount", regexp_replace(col("Amount_in_USD"), ",", "").cast("long"))

df = df.filter(col("Date").rlike("^[0-9]{2}/[0-9]{2}/[0-9]{4}$"))

df = df.withColumn("Date_clean", to_date(col("Date"), "dd/MM/yyyy"))

df = df.withColumn("year", year(col("Date_clean")))

# -------------------------
# 4️⃣ Create SQL Table
# -------------------------

df.createOrReplaceTempView("startups")

# -------------------------
# 5️⃣ Queries
# -------------------------

q1 = spark.sql(
    """
SELECT COUNT(*) AS total_startups
FROM startups
WHERE LOWER(City)='pune'
"""
)

q2 = spark.sql(
    """
SELECT COUNT(*) AS seed_startups
FROM startups
WHERE LOWER(City)='pune'
AND LOWER(InvestmentnType)
IN ('seed funding','angel funding')
"""
)

q3 = spark.sql(
    """
SELECT SUM(Amount) AS total_funding
FROM startups
WHERE LOWER(City)='pune'
"""
)

q4 = spark.sql(
    """
SELECT Industry_Vertical,
COUNT(*) AS total_startups
FROM startups
GROUP BY Industry_Vertical
ORDER BY total_startups DESC
LIMIT 5
"""
)

q5 = spark.sql(
    """
SELECT year,
Investors_Name,
SUM(Amount) AS total_investment
FROM startups
GROUP BY year, Investors_Name
ORDER BY year, total_investment DESC
"""
)

bonus1 = spark.sql("""
SELECT City,
Startup_Name,
Amount
FROM (
    SELECT City,
           Startup_Name,
           Amount,
           ROW_NUMBER() OVER(
               PARTITION BY City
               ORDER BY Amount DESC
           ) as rank
    FROM startups
) t
WHERE rank = 1
""")

bonus2 = spark.sql("""
SELECT SubVertical,
COUNT(*) as total_startups
FROM startups
GROUP BY SubVertical
ORDER BY total_startups DESC
""")

bonus3 = spark.sql("""
SELECT SubVertical,
SUM(Amount) as total_funding
FROM startups
GROUP BY SubVertical
ORDER BY total_funding DESC
""")


# -------------------------
# 6️⃣ Create Output Folder
# -------------------------

os.makedirs("output", exist_ok=True)

# --------------------------
# 7️⃣ Save Results (Using Pandas)
# -------------------------

q1.toPandas().to_csv("output/q1_pune_startups.csv", index=False)
q2.toPandas().to_csv("output/q2_seed_startups.csv", index=False)
q3.toPandas().to_csv("output/q3_total_funding.csv", index=False)
q4.toPandas().to_csv("output/q4_top_industries.csv", index=False)
q5.toPandas().to_csv("output/q5_top_investors.csv", index=False)
bonus1.toPandas().to_csv("output/bonus_top_startup_each_city.csv", index=False)
bonus2.toPandas().to_csv("output/bonus_subvertical_growth.csv", index=False)
bonus3.toPandas().to_csv("output/bonus_subvertical_funding_growth.csv", index=False)

# -------------------------
# 8️⃣ Print Schema
# -------------------------

print("\nSchema Q1")
q1.printSchema()

print("\nSchema Q2")
q2.printSchema()

print("\nSchema Q3")
q3.printSchema()

print("\nSchema Q4")
q4.printSchema()

print("\nSchema Q5")
q5.printSchema()

# -------------------------
# 9️⃣ Stop Spark
# -------------------------

spark.stop()

print("\n✅ Assignment completed successfully!")
