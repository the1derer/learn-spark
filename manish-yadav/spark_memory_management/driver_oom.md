# Spark Memory management

## Potential interview questions

1. What is out-of-memory (oom) in spark?

2. Why do we get driver oom?

3. What is driver overhead memory?

4. Commom reason to et a driver oom?

5. How to handle oom?

---> Why driver oom error in collect() but not in show()

Ans: When we use `collect()`, the data that was on different executors are brought to the JVM heap of spark driver.

But when using `show()`, only one partition is sent to JVM Heap of Driver.

## driver memory

spark.driver.memory ==> Only JVM process
spark.driver.memoryOverhead ==> Non-JVM process like storage of objects, Container

memoryOverhead is 10% of Driver-Memory. But the minimum of 384MB is allocated if 10% is less.

# Common reasons for driver oom

1. collect() method
2. Broadcast
3. More objects in used in the process
