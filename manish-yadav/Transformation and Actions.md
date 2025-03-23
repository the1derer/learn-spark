# Transformations and actions in Spark

## Potential interview questions

* What is transformation and how many types of transformations do we have?
* What happens when we use group by or join in transformation?
* How jobs are created in Spark? Action: count, show, collect


## Transformations

Any 

### Types of transformations

* Narrow dependency: Transformation where we don't have to depend on other partitions. Eg:- Filter, select, union, map etc.



* Wide dependency: Transformation where we have to depend on other parition. Since, in this case data has to be moved b/w partitions we should minimise the use of wide dependency transformations. Eg:- groupBy, reduceByKey, join, distinct etc


## Actions

Note: Whenever any action is performed, the executors submitted the computed results to the driver which then shows the results. So, be mindful when performing any actions as the result may exceed memory capacity of spark driver hence giving us `DriverOutofMemoryExecption`.