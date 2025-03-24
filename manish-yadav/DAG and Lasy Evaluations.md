# DAG and Lazy evalution in Spark


## Directed Acyclic Graphs (DAG)

Spark creates a graph of all the transformation.

All jobs have a DAG


```python

flight_data = spark.read.format("csv")\   ---> action
              .option("header","true")\
              .option("inferSchema", "true")\  ---> action
              .load("/path/to/file.csv)

flight_data_repartition = flight_data.repartition(3) ---> wide transformation

us_flight_data = flight_data.filter("DEST_COUNTRY_NAME=='United States'") ---> narrow transformation

us_india_data = us_flight_data.filter((col("ORIGIN_COUNTRY_NAME")=='India') | (col("ORIGIN_COUNTRY_NAME")=='Singapore')) ----> narrow transformation

total_flight_ind_sing = us_india_data.groupby("DEST_COUNTRY_NAME").sum("count") ---> wide transformation

total_flight_ind_sing.show() ---> action

```

