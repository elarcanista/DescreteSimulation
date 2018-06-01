import sys
import os
import datetime as dt
import re

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
    fields[0] = re.match(r"(\d+)(?:_\d+)?", fields[0]).groups()[0]
    for i in dateFields:
        fields[i] = date2TimeSince(str2Date(fields[i]), refDate)
    for i in timeFields:
        fields[i] = str2Time(fields[i])
    return fields

def insert2Dict(d, item, dates, times, key, state):
    submission = dates[0]
    start = dates[1]
    end = dates[2]
    elapsed = times[0]
    if key in d:
        prevVal = d[key]
        d[key][submission] = min(prevVal[submission], item[submission]) #submission
        d[key][start] = min(prevVal[start], item[start]) #start
        d[key][end] = max(prevVal[end], item[end]) #end
        d[key][elapsed] = d[key][end] - d[key][start]     #elapsed
        if d[key][state] != "FAILED":
            prevVal[state] = item[state]
    else:
        d[key] = item

if __name__ == "__main__":
    uniqueProcess = {}
    inF = open(sys.argv[1], "r")
    outF = open("in.out", "w")
    headers = re.findall(r"[^|\n]+",inF.readline())
    print(*headers, sep = '\t', file = outF)
    for line in inF:
        parsedLine = parse(line, [3,4,6], [5], str2Date("2017-04-26T09:24:54"))
        insert2Dict(uniqueProcess, parsedLine, [3,4,6], [5], parsedLine[0],2)

    submitDict = {}
    for key, item in uniqueProcess.items():
        insert2Dict(submitDict,item,[3,4,6],[5], item[3],2)

    for key, item in submitDict.items():
        print(*item, sep='\t', file=outF)
    inF.close()
    outF.close()
