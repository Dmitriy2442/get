import RPi.GPIO
import time

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

RPi.GPIO.setmode(RPi.GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RPi.GPIO.setup(dac, RPi.GPIO.OUT)

try:
    str = input("Enter time period: ")
    per = float(str)
    while True:
        for dec in range (255):
            bin_str = decimal2binary(dec)
            for i in range (8):
                RPi.GPIO.output(dac[i], bin_str[i])
            time.sleep(per/256/2)
        for dec in range (255):
            bin_str = decimal2binary(255 - dec)
            for i in range (8):
                RPi.GPIO.output(dac[i], bin_str[i])
            time.sleep(per/256/2)
        
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.cleanup()