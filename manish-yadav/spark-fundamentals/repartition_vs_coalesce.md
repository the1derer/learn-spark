# Repartition and Coalesce

## Potential interview Questions

* What is repartitioning in spark?

* What is coalesce in spark?

* Which one will you choose and why?

* Repartitioning vs coalesce?

## Why were repartitioning and coalesce introduced?

Let's say we have different partitions with following size on different executor:

10 MB e1
20 MB e2
30 MB e3
40 MB e4
100 MB e5

Since, it will take more time to process more data, this will lead to wastage of resources as the executors will less data will complete faster and then sit idle.

To deal with this situation we have repartition and coalesce to distribute data within different partitions.

Scenario:

Let's say we did a join. We are joining Product

Since Product data will be skewed coz some products are sold more than others. So, one of the product data will come and sit on a single executor.


### Repartition

In repartition, our data is re-shuffled and will be distributed evenly

If we repartition (5) the example data then we will have 5 partitions each of 200 MB / 5 = 40 MBs

40 MB
40 MB
40 MB
40 MB
40 MB


* Note: There will be shuffling (Hash based shuffling)

Pros:
* Evenly distributed data.

Cons:
* More I/O


Repartition can increase or decrease the number of partitions.

* We can also repartition based on a column

```python
df = df.repartition(300, "column_name")
df.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().show()
```

In the above example if we have asked to repartiton in more partition then the values in "column_name", spark will pull no records or null records in remaining partitions.


### Coalesce

Coalesce will merge the data.

If we coalesce(3) example data, we will have following:

30MB
70MB
100MB


Coalesce will not shuffle the data (TODO:How is this possible?)

Pros:

Not expensive

Cons:
Uneven data distribution. So, if we have low skewness in data.

coalesce can only decrease the partitions
