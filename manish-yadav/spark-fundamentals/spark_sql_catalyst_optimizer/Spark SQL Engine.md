# Spark SQL Engine

## Potential Interview Questions

* What is catalyst optimizer / Spark SQL engine?
* Why do we get Analysis exception error?
* What is catalog?
* What is physical planning / spark plan?
* Is spark SQL engine a compiler? ---> Yes, it compiles our code to Java byte code
* How mny phases are involved in spark SQL engine to convert code into Java byte code?

## High level view

![Catalyst Optimizer](./spark_catalyst _optimizer.png)

## Catalyst optimizer / Spark SQL engine

There are 4 phases of catalyst optimizer:

1. Analysis
2. Logical Planning
3. Physical planning
4. (Whole Stage) Code generation


code ---> unresolved logical plan ---> resolved logial plan --> optimized logical plan ---> physical plan


### Analysis phase

**What is catalog?**
Catalog is (keeps) the metadata of the data (Tables, files, databases), it checks if the files/sources existence etc.


In analysis phase of code generation, if the column/table/db is not found in catalogue then we get the `Analysis Exception`.

For example: If we try to `select`/`show` the table or column in a dataframe.

### Logical planning optimization


### Physical planning

Checks how to join the tables like `broadcast` etc.

Multiple physical plans are created.
Then cost based model is applied.

The plan which gives us best resource utilization is selected. That plan is called `Best physical plan`.

`Best physical plan` are nothing but the set of RDDs that are going to run on our cluster.


