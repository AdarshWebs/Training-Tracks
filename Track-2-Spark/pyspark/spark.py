from pyspark.sql import SparkSession

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("FirstSparkApp") \
    .getOrCreate()

# Step 2: Create data
data = [
    ("Rahul", 25, "Pune"),
    ("Priya", 30, "Mumbai"),
    ("Amit", 28, "Pune")
]

# Step 3: Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age", "City"])

# Step 4: Show data
df.show()

# Step 5: Print schema
df.printSchema()

# Step 6: Stop Spark
spark.stop()