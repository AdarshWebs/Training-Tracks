from pyspark.sql import SparkSession

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("ReadCSVExample") \
    .master("local[*]") \
    .getOrCreate()

# Step 2: Read CSV file
df = spark.read.csv("people.csv", header=True, inferSchema=True)
df.select("Name").show()
# Step 3: Show data
df.show()

# Step 4: Print schema
df.printSchema()

# Step 5: Stop Spark
spark.stop()