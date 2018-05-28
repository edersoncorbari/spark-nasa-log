## Spark Nasa Log

Churning the logs of NASA Kennedy Space Center WWW server.

You can check the page here: http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html

## Requirements

It is necessary to install Spark in your environment, the test was done in a virtual machine with [Ubuntu](https://www.ubuntu.com/) 16.04 LTS following the tutorial below:

* [Setting up Apache Spark](https://www.inertia7.com/projects/36);

To run the Python Script you do not need any special libraries, only the libraries of the own spark.

## Analyzes

* Q1. What is the number of unique hosts?

```
A1-> Number of unique hosts: 137978
```

* Q2. The total number of 404 errors?

```
A2-> Total log number 404 found = 20890
```

* Q3. Top 5 URLs that caused 404 errors?

```
A3-> Top 5 URLs that cause 404 errors:
('/pub/winvn/readme.txt', 2004)
('/pub/winvn/release.txt', 1732)
('/shuttle/missions/STS-69/mission-STS-69.html', 683)
('/shuttle/missions/sts-68/ksc-upclose.gif', 428)
('/history/apollo/a-001/a-001-patch-small.gif', 384)
```

* Q4. How many 404 errors occurred per day?

```
A4-> Number of 404 codes per day/count:
1995-07-22 - 192
1995-07-23 - 233
1995-08-20 - 312
1995-08-26 - 366
1995-07-19 - 639
1995-07-07 - 570
1995-07-05 - 497
1995-08-22 - 288
1995-07-08 - 299
1995-08-15 - 327
1995-07-03 - 474
1995-07-10 - 398
1995-08-31 - 526
1995-07-28 - 94
1995-08-11 - 263
1995-07-17 - 406
1995-08-28 - 410
1995-07-15 - 254
1995-07-09 - 348
1995-07-27 - 336
1995-07-25 - 461
1995-08-08 - 391
1995-07-18 - 465
1995-07-24 - 328
1995-08-09 - 279
1995-07-01 - 316
1995-08-23 - 345
1995-08-10 - 314
1995-08-01 - 243
1995-08-19 - 209
1995-08-16 - 259
1995-08-24 - 420
1995-07-16 - 257
1995-07-13 - 530
1995-07-14 - 413
1995-08-30 - 571
1995-08-29 - 420
1995-08-12 - 196
1995-07-04 - 359
1995-07-06 - 640
1995-08-04 - 346
1995-07-11 - 471
1995-07-20 - 428
1995-08-03 - 303
1995-08-18 - 256
1995-08-13 - 216
1995-08-27 - 370
1995-07-21 - 334
1995-08-21 - 305
1995-07-26 - 336
1995-08-14 - 287
1995-08-25 - 415
1995-08-17 - 271
1995-08-05 - 236
1995-07-02 - 291
1995-07-12 - 467
1995-08-06 - 373
1995-08-07 - 537
```
* Q5. The total number of bytes returned by clients?

```
A5-> Total bytes returned:
(count: 3460360, mean: 18935.441238194595, stdev: 73043.86403436471, max: 6823936, min: 0)
```

 ### Testing ###
 
 To test the code it is necessary to be with Spark configured as already described above, then just execute the command:
 
```shell
wget --no-cache ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz
wget --no-cache ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz
```

Now run the script in the same directory where you downloaded the files.

```shell
spark-submit main.py
```

You should get the same ![Log](https://github.com/edersoncorbari/spark-nasa-log/blob/master/main.log) result!

It's the end :-)
