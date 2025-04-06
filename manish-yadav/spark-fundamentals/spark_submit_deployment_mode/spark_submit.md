# Spark Submit

## Potential interview questions

1. What is spark-submit?

2. How do you run your job on spark cluster?

3. Where is your spark cluster?

4. What is deploy mode in spark-submit?

5. What is master in spark-submit?

6. How do you provide memory configuration and why do you use this much memory?

7. How do update configurations like broadcast threshold, timeout, dynamic memory allocation?

## What is spark-submit?

`spark-submit` is a command line tool though which we run our spark application. Through this we provide all the files and jars. spark-submit creates a package of the provided files and jars and runs it on spark cluster.


## Where is your spark cluster?

There can be multiple type of cluster:

1. Standalone cluster
2. Local
3. Kubernetes(K8)
4. YARN
5. Mesos

```
/bin/spark-submit\
  --master local[5]\ ---> Where our cluster is created i.e. local, YARN/, standalone(spark://10l160.78.10:700)
  --deploy-mode cluster\ ---> Where our driver will run. cluster or client
  --class main_call.scala \ ---> Java/Scala (optional)
  --jars /home/mysql_jar/mysql-connector.jar\ ---> comma seperated path. Recommended to use absolute path
  --conf spark.dynamicAllocation.enabled=true\
  --conf spark.dynamicAllocation.minExecutors=1\
  --conf spark.dynamicAllocation.maxExecutors=10\
  --conf spark.sql.broadcastTimeout=3600\
  --conf spark.sql.autoBroadcastJoinThreshold=100000\
  --driver-memory 1G\
  --executor-memory 2G\
  --executor-cores 2\ --> Number of parallel task that can run in an executor
  --py-files spark_session.py, logging_confg.py,...--->absolute path to dependent python files
  --files config.py\ ---> files other than python files like .config, .ini files
  /home/.../main.py testing_project dev
  ar
  ```

  Edge node ---> The machine on which user submit code or do spark-submit command.

  This machine has access to cluster machines.
