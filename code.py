import board
import time
import adafruit_dht
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn    #import analog input module

# The soil moisture sensors are on port 1, being the analog and port 4, the digital one of the franzinho    
humid_analog = AnalogIn(board.IO1)        # analog
humid_digital = DigitalInOut(board.IO4)   # digital
humid_digital.direction = Direction.INPUT # Configure pin as digital input

wait_time = 1
watering_time = 1

# Adapted according to the soil moisture sensor - value for dry land
dry_value = 51130

while True:
    try:
        # print the values read from the soil moisture sensor
        print("humid (Digital value):", humid_digital.value)
        print("humid (Analogic value):", humid_analog.value)

        time.sleep(1);

        if humid_analog.value > dry_value :
            print("Starting watering...")
            time.sleep(watering_time)
            print("Finishing watering.")
        else:
            time.sleep(wait_time)

    except RuntimeError as e:
        print("Read failure")

    time.sleep(1)