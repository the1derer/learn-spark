# Spark join strategies -- Sort and Shuffle

## Potential interview questions:

1. What are the join strategies in spark?
2. Why join is expensive/wide dependency trasformation?
3. Difference b/w shuffle hash join and shuffle sort-merge join?
4. When do we need broadcast join?

-------

* Joins are expensive because there is shuffling

Scenarios:

We have 2 dataframes of 500MBs each.

Df1             Df2

500MB/128MB = 4 partitions for each dataframes

**Note:** We have 200 partitions by default whenever we do wide body partitions.


## Strategy in spark

1. Shuffle sort-merge join
2. Shuffle hash join
3. Broadcast hash join
4. Cartesian join
5. Broadcast nested loop join (costliest join)

### Shuffle sort-merge join

After shuffling, data is sorted in both of the tables before joining

sorting --> O(n log n)

### Shuffle hash join

In this join, hash table of smaller table is created.

Hash table is created in-memory.

Hashing is done for unique-keys of the tables.

* After hashing is done, complexity is O(1)
* By default spark does, shuffle sort-merge join.
* Shuffle hash join is done only when there is enought memory in executor. otherwise we will get the OutofMemoryExeception
