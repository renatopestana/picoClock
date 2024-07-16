from machine import RTC


rtc = RTC()


def setTimeRTC(tm):
    rtc.datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
    print(rtc.datetime())


def getTimeRTC():
    return rtc.datetime()
    

def checkAlarmRTC(set_year,set_month,set_day,set_hour,set_minute):
    time = rtc.datetime()
    if set_year == int(time[0]) and set_month == int(time[1]) and set_day == int(time[2]) and set_hour == int(time[4]) and set_minute == int(time[5]):
        print("ALARM")
    else:
        print("Time not reached")
        print("time now " + str(time))
        print("time to alarm:  " + str(set_year) +" " + str(set_month) + " " + str(set_day) + " " + str(set_hour) + " " + str(set_minute))

