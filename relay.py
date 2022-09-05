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
'''
if __name__ == '__main__':
    try:
        motor_on(channel)
        time.sleep(1)
        motor_off(channel)
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
'''
temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
while True:
    if temp > 23.5:
        channel = 21
        motor_on(channel)
        time.sleep(180)
        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
    else:
        channel = 21
        motor_off(channel)
        time.sleep(180)
        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1_slave")
#def get_temp(dev_file):
#    f = open(dev_file,"r")
#    contents = f.readlines()
#    f.close()
#    index = contents[-1].find("t=")
#    if index != -1 :
#        temperature = contents[-1][index+2:]
#        cels =float(temperature)/1000
#        return cels
# Parse command line parameters.
#sensor_args = { '11': Adafruit_DHT.DHT11,
#                '22': Adafruit_DHT.DHT22,
#                '2302': Adafruit_DHT.AM2302 }
#if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#    sensor = sensor_args[sys.argv[1]]
#    pin = sys.argv[2]
#else:
#    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
#    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
#    sys.exit(1)')
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#while 0<1:
#
#       if humidity is not None and temperature is not None:
#                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, >
#                if __name__ == "__main__":
#                        temp = get_temp("/sys/bus/w1/devices/28-3c01a816dc0b/w1>
#                        print(temp)
#                time.sleep(1)
#        else:
#                print('Failed to get reading. Try again!')
#                sys.exit(1)

