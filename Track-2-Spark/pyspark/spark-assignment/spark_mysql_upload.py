from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace

# Start Spark Session
spark = (
    SparkSession.builder
    .appName("StartupMySQLUpload")
    .master("local[*]")
    .config("spark.jars", "mysql-connector-j-9.6.0.jar")
    .getOrCreate()
)

# -----------------------------
# 1. READ CSV FILE
# -----------------------------

df = spark.read.csv(
    "data/startup.csv",
    header=True,
    inferSchema=True
)

print("Original Data")
df.show(5)

# -----------------------------
# 2. TRANSFORM DATA
# -----------------------------

df_clean = df.withColumn(
    "startup_name_processed",
    regexp_replace(col("Startup_Name"), " ", "")
)

df_clean = df_clean.withColumn(
    "City",
    lower(col("City"))
)

print("Transformed Data")
df_clean.show(5)

print("Schema")
df_clean.printSchema()

# -----------------------------
# 3. WRITE DATA TO MYSQL
# -----------------------------

df_clean.write.format("jdbc") \
.option("url", "jdbc:mysql://localhost:3306/startup_db") \
.option("driver", "com.mysql.cj.jdbc.Driver") \
.option("dbtable", "startup_data") \
.option("user", "root") \
.option("password", "adarsh02022004") \
.mode("overwrite") \
.save()

print("Data successfully uploaded to MySQL")

spark.stop()