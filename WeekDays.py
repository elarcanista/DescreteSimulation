#!/bin/env python

import sys
import datetime as dt

def main():
    data = open(sys.argv[1], "r")
    count = 0
    for line in data:
        data_line = line.split(",")
        date = list(map(int, data_line[1:-2]))
        print(data_line[0],*date,dt.datetime(*date).weekday(), data_line[7], data_line[8].strip())

if __name__ == '__main__':
   main()
