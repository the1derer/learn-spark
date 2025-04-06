# Broadcast hash join (TODO: Redo all the practicals in the video)

## Potential interview questions:

1. Why do we need broadcast hash join?

To remove shuffling.

2. How does broadcast join works?


3. Difference b/w broadcast hash join and shuffle hash join?

In Shuffle hash join, shuffling occurs. In broadcast hash join, we broadcast the data

4. How can we change broadcast size of table? Or what is te default size?

Default size in 10MB.

`spark.conf.get("spark.sql.autoBroadcastJoinThreshold")` ---> Will provide in bytes

`spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)` --> will disable broadcast join threshold


5. When broadcast table is not good or it will fail?

When we try to broadcast big data. Leading to memory issues.

---

## What is broadcast hash join

broadcast ---> Taking something and spreading it everywhere (eg. tv broadcasting)

hash --> hashing of smaller table


driver 

* Broadcast join only works when one table is big and another table is smaller.

* By default in Spark, tables smaller than 10MBs are considered as small tables and broadcasted.

Eg.---> We have a 5MB small table and 1 GB bigger table.

Now, this 1GB table are distributed among many executors. Since size of 1 block is 128MB, 1000MB/128MB = 8 blocks/partitions. These partitions can be distributed among many executors.

If there is no broadcasting, 1GB data will move around to match with smaller 5MB table, hence creating a lot of shuffling. This will choke cluster.

----
Now, lets send 5MB table data to every executor.

So, there will be no movement of data b/w executors hence removing need for shuffling.

The work to send this 5MB smaller file to every executor is done by Spark Driver.
So, for Spark Driver to be able to store and send this data, Driver need to have the needed space for this.

If we try to broadcast large file, we could end up with `Driver OutofMemory Error`.

Another issue with broadcasting large size file is that it will consume lot of network bandwidth slowing the network.

Also, after broadcasting large files on all executor will lead to storage and memory issues in executors too.

**Note:** So decide the broadcast size wrt your cluster.

SBroadcast will improve the performance but could lead to memory issues, so we need to be be mindful when doing broadcast

`Dataframe.explain()` ---> Shows the Spark physical plan.

* In Spark, the prefered way is `sort merge join`
