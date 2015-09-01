#!/usr/bin/python
#Python script including MCP3008 read
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip. Channel must be an integer between 0 and 7
# ReadChannel function - Needs an argument named channel 
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level, rounded to specified number of decimal places.
# ConvertVolts function - Needs two arguments named data and places(number of decimal palces)
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(data,places)
  return data
 
# Function to calculate distance from SHARP IR sensor data, rounded to specified number of decimal places.
def ConvertDistance(data,places):
	d = 16.2537 * data**4 - 129.893 * data**3 + 382.268 * data**2 - 512.611 * data + 306.439
	cm = int(round(d,places))
    #val = '%d cm' % cm
    #percent = int(cm/1.5)  
	return cm
 
# Define sensor channels
Sharp_1=1
 
# Define delay between readings
delay = 1
 
while True:
 
  # Read the Sharp IR sensor data
  Sharp_level = ReadChannel(Sharp_1)
  Sharp_volts = ConvertVolts(Sharp_level,2)
  Sharp_dist = ConvertDistance(Sharp_level,2)
 
  # Print out results
  print "--------------------------------------------"
  print("Distance: {} ({}V)".format(Sharp_level,Sharp_volts,Sharp_dist))
  #print("Temp : {} ({}V) {} deg C".format(temp_level,temp_volts,temp))
 
  # Wait before repeating loop
  time.sleep(delay)