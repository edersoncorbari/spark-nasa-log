#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file main.py
#
# Implementations to main spark script.
#
# PYSPARK - Analysis of NASA Kennedy Server Logs.
#
# Copyright (c) 2018 Ederson de Moura Corbari
#
# @author Ederson de Moura Corbari
#
# $Id: EDMC Exp$
#

import re

from datetime import datetime

from pyspark import SparkContext
from pyspark import SparkConf


class NasaLogAnalysis(object):

    def __init__(self):
        self.__info = self.__class__.__module__ + '.' + self.__class__.__name__
        self.__conf = SparkConf().setAppName(str(self.__info)).setMaster('local[*]')
        self.__files = 'NASA_access*' 

    def find_log(self, l):
        m = re.search('^(\S+) (\S+) (\S+) \[(\S+) [-](\d{4})\] "(\S+)\s*(\S+)\s*(\S+)\s*([/\w\.\s*]+)?\s*"* (\d{3}) (\S+)', l)
        if m is None:
            m = re.search('^(\S+) (\S+) (\S+) \[(\S+) [-](\d{4})\] "(\S+)\s*([/\w\.]+)>*([\w/\s\.]+)\s*(\S+)\s*(\d{3})\s*(\S+)', l)
        if m is None:
            return (l, 0)
        else:
            return (l, 1)

    def map_log(self, l):
        m = re.search('^(\S+) (\S+) (\S+) \[(\S+) [-](\d{4})\] "(\S+)\s*(\S+)\s*(\S+)\s*([/\w\.\s*]+)?\s*"* (\d{3}) (\S+)', l)
        if m is None:
            m = re.search('^(\S+) (\S+) (\S+) \[(\S+) [-](\d{4})\] "(\S+)\s*([/\w\.]+)>*([\w/\s\.]+)\s*(\S+)\s*(\d{3})\s*(\S+)', l)
        return (m.groups())

    def day_month(self, l):
        date_time = l[3]
        return datetime.strptime(date_time[:11], "%d/%b/%Y")

    def printf(self, m: str) -> None:
        print('\033[32m' + m + '\033[0m')

    def int2long(self, x) -> int:
        x = re.sub('[^0-9]', "", x) 
        if x == "":
            return 0
        else:
            return int(x)

    def run(self) -> int:
        sc = SparkContext.getOrCreate(self.__conf)
        rd0 = sc.textFile(self.__files)

        rd1 = rd0.map(lambda l: self.find_log(l)).filter(lambda l: l[1] == 1).map(lambda l : l[0])
        rd2 = rd1.map(lambda l: self.map_log(l))

        self.printf('-> Number of unique hosts: ' + str(rd2.map(lambda l: l[0]).distinct().count()))
        self.printf('-> Total log number 404 found = ' + str(rd2.filter(lambda l: l[9] == '404').count()))

        l0 = (rd2.filter(lambda l: l[9] == '404').map(lambda l: (l[6], 1)).reduceByKey(lambda a, b: a+b).takeOrdered(5, lambda x: -x[1]))
        self.printf('-> Top 5 URLs that cause 404 errors:')
        for i in l0:
            self.printf(str(i))

        l0 = (rd2.filter(lambda l: l[9] == '404').map(lambda l: (self.day_month(l), 1)).reduceByKey(lambda a, b: a+b).collect())
        d = [x[0] for x in l0]
        c = [x[1] for x in l0]
        self.printf('-> Number of 404 codes per day/count:')
        for a, b in zip(d, c):
            self.printf(str(a.strftime("%Y-%m-%d")) + ' - ' + str(b))

        l0 = rd2.map(lambda l: self.int2long(l[-1])).stats()
        self.printf('-> Total bytes returned:')
        print(l0)

        return 0

def main() -> int:
    return NasaLogAnalysis().run()

if __name__ == "__main__":
    main()

