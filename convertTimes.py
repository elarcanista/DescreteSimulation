import sys
import os
import datetime as dt
import re
import csv

def date2TimeSince(date, refDate):
    return int((date-refDate).total_seconds())

def str2Date(strDate):
    dateFormat = r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})"
    date = re.match(dateFormat, strDate).groups()
    date = dt.datetime(*map(int,date))
    return date

def str2Time(strTime):
    timeFormat = re.compile(r"(?:(\d{1,2})-)?(\d{2}):(\d{2}):(\d{2})")
    time = re.match(timeFormat, strTime).groups()
    time = dt.timedelta(
            days = 0 if not time[0] else int(time[0]),
            hours = int(time[1]),
            minutes = int(time[2]),
            seconds = int(time[3]))
    return int(time.total_seconds())

def parse(line, dateFields=[], timeFields=[], refDate=dt.datetime(1,1,1)):
    fields = re.findall(r"[^|\n]+",line)
    for i in dateFields:
        fields[i] = date2TimeSince(str2Date(fields[i]), refDate)
    for i in timeFields:
        fields[i] = str2Time(fields[i])
    return fields

if __name__ == "__main__":
    for i in range(1,len(sys.argv)):
        inF = open(sys.argv[i], "r")
        outF = open(os.path.splitext(sys.argv[i])[0]+'.out', 'w')
        inF.readline()
        for line in inF:
            parsedLine = parse(line, [5,6,8], [4,7], dt.datetime(2018,1,1))
            print(*parsedLine, sep='\t', file=outF)
        inF.close()
        outF.close()
