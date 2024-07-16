from time import sleep
from random import randint
from wlan import connectWiFi
from ntp import getTimeNTP
from real_time_clock import setTimeRTC, getTimeRTC
from clock import setBrightness, refreshClock
from tools import rjust, ljust


# Starts clock with red dashs until gets connected
refreshClock("----", 1, False)

# Connect to WiFi network
connectWiFi()
# Wait for a second
sleep(1)
# Get updated time from NTP server
tm = getTimeNTP()
# Adjust RTC according to NTP info
setTimeRTC(tm)
print('RTC updated:', getTimeRTC())


dotState = False

# Main loop
while True:
    # get current date and time from RTC
    dh = getTimeRTC()
    print(dh)
    # Get hour and minute to show
    hour = int(dh[4])
    minute = int(dh[5])
    current_time = rjust(str(hour), 2, "0") + rjust(str(minute), 2, "0")
    dotState = not dotState
    # Refresh clock display
    refreshClock(current_time, hour+1, dotState)
    # Wait for a second
    sleep(0.5)

