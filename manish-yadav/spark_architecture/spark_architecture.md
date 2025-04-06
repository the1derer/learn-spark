# Spark Architecture

Libraries / High Level API ---> Low level APIs (Spark Core) ---> Spark Engine

Spark Engine requests Cluster Manager for resources.

It is the responsibility of cluster manager to interact with the hardware to provide requested resources for Spark engine.

Examples of Cluster Manager: YARN, Mesos, Kubernetes, Standalone Cluster


**Question** What is a cluster?
Answer: Many network connected computers are known as clusters

## Detailed View

Cluster works in Master-Slave(or Master-Worker) architecture.

* On Master there is YARN installed, which is called **Resource Manager**.

All the worker nodes are called Node Manager.

* Resource Manager will will request one of the worker nodes to create a container for driver.

* Now in this driver-container in Spark is known as **application master**.

Application Master requests Resource Manager to provide resources for executors.

In this Application Master following process will run:
  Python --> PySpark
  Java/Scala ---> JVM main()

* Since Spark is written in Scala and Scala is a JVM language which means Spark will run on JVM.

* Since Python is not a JVM language. In case of PySpark, PySpark main method calls JVM main method.

* Inside Spark core there are different wrapper for different programming languages.

There is Java wrapper, and there is python wrapper.

Python wrapper goes to Java Wrapper which in-turn goes to Spark Core.

This JVM `main()` method is known as **Application Driver**.


## Executor container:

* In every executor container there is JVM process that runs.

* In case of PySpark, if there is any UDF function defined, then we need Python at runtime, to handle this we have a 'Python worker' installed on every executor

* That is why we should lessen the use of UDF to decrease impact on performance.
