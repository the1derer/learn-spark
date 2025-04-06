import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.function import *

spark = SparkSession.builder.master("local[5]")\
        .appName("testing")\
        .config("spark.driver.memory", "1g")
        .getOrCreate()
print(spark) # spark object

spark2 = spark.newSession() # new spark session creation
print(spark2)
sc = spark.sparkContext # getting spark context
print(sc)

employee_df = spark.read.format("csv")\
                .option("header", "true")\
                .option("inferSchema", "true")\
                .option("mode", "PERMISSIVE")\
                .load("/path/to/employee_data.csv")

employee_df = employee_df.repartition(3)
employee_df = employee_df.filter(col("salary")>90000).select("age", "salary")

employee_df.show()
input("Press enter to terminate")
