import machine
import network
from time import sleep

ssid = 'CHACARAWE'
password = '#cafesemdoce$'

def connectWiFi(max_wait=10):
    n=0
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
        
    print('Waiting for connection')
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        n+=1
        if n>max_wait:
            machine.reset()
        sleep(1)
        
    print(wlan.ifconfig())

