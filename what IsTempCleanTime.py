#!/usr/bin/python

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)


# Loop printing measurements every second.
print('Press Ctrl-C to quit.')

while True:
    temp = sensor.readTempC()
    ts = time.time()
    internal = sensor.readInternalC()
    print('Thermocouple Temperature at '+ str(ts) + ' = ' + str(temp) +'*C')
    time.sleep(1.0)
