# Executor out-of-memory

## Potential interview questions

1. Why do we get OOM when data can be spilled to the disk?

2. How spark manages storage inside executor internally?

3. How task is split in executor?

We can run the number of task in parallel as there are number of cores.

If we give more than 5 cores, there is chance of memory overhead error as there it will now have to handle more objects and  

So, recommended is 3-5 cores per executors.

4. Why do we need overhead memory?

5. When do we get executor OOM?

6. Types of memory manager in spark?

Unified (1.6.0+) and static(before 1.6.0)

## Memory in Spark executor

spark.executor.memory = 10GB ==> JVM process
spark.executor.memoryOverhead = 10% of executor-memory ==> Non-JVM  + Container (300-400MBs)

If any of these limit is exceeded, we get Executor OOM exception

## Overhead memory

1. Used for non-JVM processes.
2. 300-400MBs is used by container
3. 600-700MB will be used by PySpark applications.

## spark.executor.memory (JVM process memory)

###  Reserved Memory

 ==> 40% of remaining memory after 'User memory'

  * It is used to store Spark internal objects.
  * used by spark engine.

Note: Executor memory should be at least 1.5 times the memory of Reserved memory.

### Spark Memory

 ==> 60% of remaining memory after 'User memory'

This is further divided into 2 parts:-

#### Storage Memory Pool (50%)

* It is used for storing intermediate state of tasks like joining, caching etc
* It is used to store cached data.
* Memory eviction is done in LRU(Least recently used) fashion.

#### Executor Memory Pool (50%)

* It is used for storing object that is required during execution of spark task.
* Store hash table for hash aggregation.
* Short lived --> cleared after each operation.
* Spilling to disk.

### Memory manager

#### Static Memory manager.
Old. Used to set 50% hard boundary for storage.

#### Unified Memory manager
Both memories are unitified. If one is full and other is empty, empty of other memory is used by other.

There is no hard memory

### User memory

==> 300 MB fixed

  * It is used to store user defined data structure, spark internal metadata and any UDF created.
  * This is used by RDD operation.
  Eg. Aggregation --> map, partition, transformation



## When we can't evict or spill to disk?

When there is data skewed