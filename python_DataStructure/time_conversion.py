#!/bin/python

import sys

def timeConversion(s):
    ret=""
    # Complete this function
    time=s.split(":")
    if len(time) < 3:
        return "NOT a valid input not a time mode \n"
    try:
        hour = int(time[0])
    except:
        return "NOT a valid input hour is not currect \n"
    hour=int(time[0])
    if (time[2][-2:] != "PM" and time[2][-2:] != "AM") or int(time[0])>12 or int(time[0])<1 or int(time[1])>59 or int(time[1])<0 or int(time[2][:-2])>59 or int(time[2][:-2])<0:
        return "NOT a valid input \n"
    Apm=time[2][-2:]
    if Apm=="PM" and int(time[0])<12:
        hour += 12
    elif hour == 12 and Apm == "AM":
        hour -= 12
    if hour>24:
        hour=hour-24
    hours=""
    minutes=""
    seconds=""
    if hour<10:
        hours="0"
    hours+=str(hour)
    if int(time[1])<10:
        minutes += "0"
    minutes += str(int(time[1]))
    if int(time[2][:-2])<10:
        seconds += "0"
    seconds += str(int(time[2][:-2]))

    ret += hours
    ret += ":"
    ret += minutes
    ret +=":"
    ret += seconds
    return ret
while(1):
    s = raw_input().strip()
    result = timeConversion(s)
    print(result)
