import sys
import RPi.GPIO as GPIO
import time
channel = 21
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
def get_temp(dev_file):
    f = open(dev_file,"r")
    contents = f.readlines()
    f.close()
    index = contents[-1].find("t=")
    if index != -1 :
        temperature = contents[-1][index+2:]
        cels =float(temperature)/1000
        return cels

if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
        motor_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
while temp>10:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    if temp > 23.5:
        motor_on(channel)
        time.sleep(60)
        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
        GPIO.cleanup()
    else:
        motor_off(channel)
        time.sleep(60)
        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
        GPIO.cleanup()

