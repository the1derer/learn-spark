# Spark sessions and Context

Both Spark session and context both provide entry into the spark cluster.

## How it works:

Like in C++/C/Java we have a main method that is entry into the program.

Similarly, in Spark, to run the code in a spark cluster we need to create spark session. We have mentioned in our code how much resources like memory and core we need. 

After we pass the arguments, a session is created and given to us. We work on this spark session.


#### Spark Context

Until Spark 1.0 we needed to create different spark contexts.

Spark context in a way is like main method.

Like, there is separate spark context for entry into context. To use SQL there was SQL context. For using Hive there was Hive context. For streaming there was Streaming Context

Now after Spark 1.0, everything is encapsulated in one Spark Session. Just create one Spark session and get all the contexts.

Example:

[code example](./job_stage_testing.py)