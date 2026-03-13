import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object StartupMySQLUpload {

  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder()
      .appName("StartupMySQLUpload")
      .master("local[*]")
      .getOrCreate()

    println("Spark Started")

    // Read CSV
    val df = spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("data/startup.csv")

    println("Original Data")
    df.show(5)

    // Transform data
    val df_clean = df
      .withColumn(
        "startup_name_processed",
        regexp_replace(col("Startup_Name"), " ", "")
      )
      .withColumn(
        "City",
        lower(col("City"))
      )

    println("Transformed Data")
    df_clean.show(5)

    println("Schema")
    df_clean.printSchema()

    // Upload to MySQL
    df_clean.write
      .format("jdbc")
      .option("url", "jdbc:mysql://localhost:3306/startup_db")
      .option("driver", "com.mysql.cj.jdbc.Driver")
      .option("dbtable", "startup_data_scala")
      .option("user", "root")
      .option("password", "adarsh02022004")
      .mode("overwrite")
      .save()

    println("Data uploaded to MySQL")

    spark.stop()

  }
}