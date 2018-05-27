## Spark Nasa Log

Churning the logs of NASA Kennedy Space Center WWW server.

In the address below we can download the datasets of the server NASA Kennedy to do some analysis using PySpark.

## Requirements

It is necessary to install Spark in your environment, the test was done in a virtual machine with [Ubuntu](https://www.ubuntu.com/) 16.04 LTS following the tutorial below:

* [Setting up Apache Spark](https://www.inertia7.com/projects/36);

To run the Python Script you do not need any special libraries, only the libraries of the own spark.

## Analyzes

* Q1. What is the number of unique hosts?

```shell
A1-> Number of unique hosts: 137978
```

* Q2. The total number of 404 errors?

```shell
A2-> Total log number 404 found = 20108
```

* Q3. Top 5 URLs that caused 404 errors?

A3 = xxx

* Q4. How many 404 errors occurred per day?

```shell
A4-> Number of 404 codes per day/count:
1995-08-28 - 820
1995-08-20 - 624
1995-08-09 - 558
1995-08-22 - 576
1995-08-31 - 1052
1995-08-26 - 732
1995-08-15 - 654
1995-08-11 - 526
1995-08-08 - 782
1995-08-23 - 690
1995-08-07 - 1074
1995-08-03 - 606
1995-08-06 - 746
1995-08-10 - 628
1995-08-29 - 840
1995-08-17 - 542
1995-08-18 - 512
1995-08-21 - 610
1995-08-27 - 740
1995-08-19 - 418
1995-08-16 - 518
1995-08-24 - 840
1995-08-25 - 830
1995-08-01 - 486
1995-08-30 - 1142
1995-08-14 - 574
1995-08-12 - 392
1995-08-05 - 472
1995-08-13 - 432
1995-08-04 - 692
```
* Q5. The total number of bytes returned by clients?

A5 = AA

