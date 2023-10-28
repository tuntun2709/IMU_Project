import time
import network
import ussl
import os
from machine import Pin
from umqtt.simple import MQTTClient
from time import sleep
from bno055 import *


### Blink the onboard LED to show startup
led = Pin("LED", Pin.OUT)

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))  # EIO error almost immediately
imu = BNO055(i2c)

topic = 'mqtt1'
calib_status_subtopic = f'{topic}/calib_status'
calib_subtopic = f'{topic}/calib'
data_subtopic = f'{topic}/data'

### Connect to WiFi
print('----------------------------------------------------------------------------------------------')
ssid = 'RPiHotspot'
password = '1234567890'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for WiFi connection or failure
connected = False
attempt = 0
while not connected and attempt < 7:
    attempt += 1
    if wlan.status() < 0 or wlan.status() >= 3:
        connected = True
    if not connected:
        led.value(not led.value())
        print("Connection attempt failed: " + str(attempt))
        time.sleep(1)
    else:
        print("Connected on attempt: " + str(attempt))

if not connected or wlan.ifconfig()[0] == "0.0.0.0":
    # Blink LED to show there is a WiFi problem
    for i in range(10):
        led.value(not led.value())
        time.sleep(0.1)
    print("Bad WiFi connection: " + wlan.ifconfig()[0])
    led.value(0)
    while True:
        pass
        


# As we end up here, we now we have a WiFi connection
print("WiFi status: " + str(wlan.ifconfig()))


### Connect to HiveMQ Cloud
broker = '192.168.50.10'
mqtt_username = 'pico1'
mqtt_key = '1234'
print('----------------------------------------------------------------------------------------------')
print("Connecting to " + broker + " as user " + mqtt_username)


sslparams = {'server_hostname': broker}

mqtt_client = MQTTClient(client_id="pico1",
                        server=broker,
                        port= 1883,
                        user=mqtt_username,
                        password=mqtt_key,
                        keepalive=3600)
con = True
while con:
    try:
        print('MQTT connecting...')
        mqtt_client.connect()
        print('MQTT Broker connected')
        con = False
    except:
        for i in range(20):
            led.value(not led.value())
            time.sleep(0.1)
        led.value(0)
        while True:
            pass
# print('Connected to MQTT Broker: ' + broker)

### Main program

calibrated_data_file = 'calibrated_data.txt'
# define messages formats to send
uncalibrated_mess = 'a'
calibrated_mess = 'b'

#define timers
timer1 = machine.Timer()
timer2 = machine.Timer()

# send calib status funcion for timer2
def calibration(timer):
    led.value(not led.value())
    calib_mess = 'sys {} gyro {} acc {} mag {}'.format(*imu.cal_status())
    mqtt_client.publish(calib_subtopic, calib_mess)
    # print(calib_mess)

# send data function for timer1
def blink(timer):
    led.value(not led.value())
    data_mess = 'Heading {:4.2f} roll {:4.2f} pitch {:4.2f}'.format(*imu.euler())
    mqtt_client.publish(data_subtopic, data_mess)
    # print(data_mess)

# try to open calib offsets file, if fail then pass
try:
    with open(calibrated_data_file, 'rb') as f:
        calibrated_data = f.read()
        imu.set_offsets(calibrated_data)
        f.close()
except:
    pass

# check calib status, if not calibrated then send status and start timer2     
calib = imu.calibrated()
if not calib:
    mqtt_client.publish(calib_status_subtopic, f'{uncalibrated_mess}', retain = True)
    timer2.init(period=500, mode=machine.Timer.PERIODIC, callback=calibration)
    while not calib:
        calib = imu.calibrated()
        time.sleep(0.7)
# when calibrated, stop timer and save the calibrated offsets 
    timer2.deinit()
    with open(calibrated_data_file, 'wb') as f:
        f.write(imu.sensor_offsets())
        f.close()
       
# print('imu is calibrated')
mqtt_client.publish(calib_status_subtopic, f'{calibrated_mess}', retain = True)
# start timer1
timer1.init(period=20, mode=machine.Timer.PERIODIC, callback=blink)

while True:
    pass
