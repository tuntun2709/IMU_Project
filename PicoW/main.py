import time
import network
import ussl
import os
from machine import Pin
from umqtt.simple import MQTTClient
from time import sleep
from bno055 import *


### Blink the onboard LED to show startup
led_red = Pin(16, Pin.OUT)
led_green = Pin(20, Pin.OUT)
led_blue = Pin(21, Pin.OUT)

topic = 'mqtt4'
calib_status_subtopic = f'{topic}/calib_status'
calib_subtopic = f'{topic}/calib'
data_subtopic = f'{topic}/data'

try:
    i2c = machine.I2C(1, sda=machine.Pin(26), scl=machine.Pin(27))  # EIO error almost immediately
    imu = BNO055(i2c)
except:
    led_red.on()
    time.sleep(1)
    led_red.off()
    while True:
        pass
    
led_green.on()
time.sleep(1)
led_green.off()

### Connect to WiFi
print('----------------------------------------------------------------------------------------------')
ssid = 'RPiHotspot'
password = '1234567890'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
try:
    wlan.connect(ssid, password)
except:
    for i in range(10):
        led_red.toggle()
        time.sleep(0.1)
    print("Bad WiFi connection: " + wlan.ifconfig()[0])
    led_red.off()
    while True:
        pass

# Wait for WiFi connection or failure
connected = False
attempt = 0
while not connected and attempt < 10:
    attempt += 1
    if wlan.status() < 0 or wlan.status() >= 3:
        connected = True
    if not connected:
        led_blue.toggle()
        print("Connection attempt failed: " + str(attempt))
        time.sleep(1)
    else:
        print("Connected on attempt: " + str(attempt))

led_blue.off()
if not connected or wlan.ifconfig()[0] == "0.0.0.0":
    # Blink LED to show there is a WiFi problem
	for i in range(10):
		led_red.toggle()
		time.sleep(0.1)
	print("Bad WiFi connection: " + wlan.ifconfig()[0])
	led_red.off()
	while True:
	    pass
        


# As we end up here, we now we have a WiFi connection
print("WiFi status: " + str(wlan.ifconfig()))


### Connect to HiveMQ Cloud
broker = '192.168.50.10'
mqtt_username = 'pico4'
mqtt_key = '1234'
print('----------------------------------------------------------------------------------------------')
print("Connecting to " + broker + " as user " + mqtt_username)


sslparams = {'server_hostname': broker}

mqtt_client = MQTTClient(client_id="pico4",
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
            led_red.toggle()
            time.sleep(0.1)
        led_red.off()
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
    led_green.toggle()
    calib_mess = 'sys {} gyro {} acc {} mag {}'.format(*imu.cal_status())
    mqtt_client.publish(calib_subtopic, calib_mess)
    # print(calib_mess)

# send data function for timer1
def blink(timer):
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
# when calibrated, stop timer and save the calibrated offsets 
    timer2.deinit()
    with open(calibrated_data_file, 'wb') as f:
        f.write(imu.sensor_offsets())
        f.close()
    led_green.on()
    time.sleep(1)
    led_green.off()

# print('imu is calibrated')
mqtt_client.publish(calib_status_subtopic, f'{calibrated_mess}', retain = True)
for i in range(4):
    led_green.toggle()
    time.sleep(0.2)
# start timer1

led_green.on()
timer1.init(period=20, mode=machine.Timer.PERIODIC, callback=blink)

while True:
    pass
