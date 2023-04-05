import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(troyka, RPi.GPIO.OUT)
RPi.GPIO.setup(comp, RPi.GPIO.IN)
RPi.GPIO.output(troyka, 1)

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for dec in range (255):
        bin_str = decimal2binary(dec)
        for i in range (8):
            RPi.GPIO.output(dac[i], bin_str[i])
        time.sleep(0.0007)
        if RPi.GPIO.input(comp) == 0:
            return dec
    return 256

try:
    while True:
        dec = adc()
        print(dec, dec/256*3.3)
        
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.output(troyka, 0)
    RPi.GPIO.cleanup()
        