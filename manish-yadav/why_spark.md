In the beginning the data was only in Structured format i.e. only in row-column form.

This data was stored in databases like Oracle, MySQL etc.

But with the internet the data came in un-sturctured format i.e. file, text, csv, image, video

There are also semi-structured format like JSON and YAML.

Databases were not able to handle these un/semi-structured.

## Big Data

The big data concept was brought to handle these issues with Databases.

### 3 V's of Big Data

i. Velocity --> Rate of incoming data
ii. Variety --> Structured, semi-structured, unstructured 
iii. Volume --> Volume of data i.e. 5GB, 10GB, 10TB

## ETL v/s ELT

ETL ---> Extract, Transform and Load
ELT ---> Extract, Load and Transform

ELT is now used for data lakes as the volume/velocity of data now a days is very large. Current rate of computation is not able to match the velocity/volume of incoming data.

## Issues

1. Storage
2. Processing --> RAM and CPU


Approaches/Option to address these issue:

1. Monolitic approach
2. Distributed approach


Limitatiomn with Monolithic approach:

* Vertical Scaling
* Expensive
* Low availability (single point of failure)

Distributed approach:

* Horizontal Scaling
* Economical
* High availability

## Distributed Approach

### Hadoop

### Spark