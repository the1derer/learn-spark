# Resilient Distributed Datasets (RDDs)

## Potential interview questions:-

1. What is RDD?
2. When do we need an RDD? ---> Full control on our data. Un-structured data
3. Features of RDD? ---> Immutable, lazy, optimization
4. What is dataframe/dataset? ---> It is a stuctured API. Data is form of column-row or key-value.
5. Why we should not use an RDD? ---> 

## What is a RDD?

Resilient Distributed dataset

RDD is a Data structure that works in spark.

For explanation:

Let's take example of list:

List = [5, 6, 10, 2, 7, 8]

list[0] = 5

now list is stored continuously on RAM.


**RDD structures the data differently.**

becoz RDD keeps the data on cluster

Example:
Let's assume we have 500MBs of data. Now, we know the block size is of 128MBs on HDFS

S0, 500MB/128MB = 4 partitions

These partitions are stores at different locations.

Now, Spark brings all these data comes to RAM.
Since, this data is distributed among different parts of cluster.

Now, how we handle this data is called RDD.

### Understanding terms of RDD

#### Resilient: In case of failure, it can recover.

* DAG ---> 

* RDD is immutable. This means it doesn't change.


RDD          ---age>18-->  RDD1 ---id<10--> RDD2


id name age

This means that RDD doesn't change to RDD1. Instead a new RDD1 is created with filtered data. Similarly, a new RDD2 is created from RDD1 with filtered data.

For all these transformation, since spark has lazy evaluation, a DAG is created.

Since, RDD is immutable, the advantage is that if any step for example RDD1 is failed. DAG (lineage) knows how to create RDD1.

RDD1 is recreated.

That is why RDD is fault-tolerent.

#### Distributed: Data is distributed over the cluster.

#### Dataset: Actual data.


### Disadvantages of RDD

* No optimization done by spark. If we write optimized code by ourselves then good otherwise there will be no optimization. Flexibility


### Advantages of RDD

* Unstructured data.
* Type safe ---> Gives error at the time of compilation.

#### Complexity of writing RDD code

**Dataframe**
```
data.groupBy("dept").avg("age")
```

Have optimiztion and good readability

**SQL**
```
select dept, avg(age) from data group by 1
```
since easy to write so can be written by Data analyst.

**RDD**
```
data.map{case (dept, age) => dept -> (age, 1)}
.reduceByKey {case ((a1, c1), (a2, c2) => (a1 + a2, c1 + c2))}
.map { case(dept, (age, c)) => dept -> age / c }
```

Difficult to write and written by Data Engineer.

#### How-to & What-to

RDD ---> How to do
Dataframe ---> What to do

Since, while using RDDs, we need to tell how to perform task, in what steps to perform the task to have optimization, it is generally preferred not to use RDDs.
