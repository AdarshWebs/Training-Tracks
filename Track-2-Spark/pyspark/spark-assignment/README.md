# Spark Startup Analysis Assignment

This project analyzes startup funding data using Apache Spark.

## Requirements

- Python 3.x
- PySpark
- Pandas

Install dependencies:

pip install pyspark pandas

## Project Structure

spark-assignment/

spark_analysis.py -> Main Spark job  
run.sh -> Script to execute job  
data/ -> Input CSV files  
/output -> Generated results  

## How to Run

Step 1: Place input files in data folder

data/startup.csv  
data/consumerInternet.csv  

Step 2: Run bash script

./run.sh

## Output

Results will be generated in:

/output

Each question output will be stored in separate folders.

## Queries Implemented

1. Startups in Pune
2. Pune Seed/Angel funding
3. Total funding in Pune
4. Top industries in India
5. Top investors by year

Bonus:
- Top startup by city
- SubVertical growth by startups
- SubVertical growth by funding