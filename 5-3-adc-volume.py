import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

RPi.GPIO.setup(dac, RPi.GPIO.OUT)
RPi.GPIO.setup(leds, RPi.GPIO.OUT)
RPi.GPIO.setup(troyka, RPi.GPIO.OUT)
RPi.GPIO.setup(comp, RPi.GPIO.IN)
RPi.GPIO.output(troyka, 1)

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    S = 0
    for i in range (8):
        S = int(S + pow(2, (7-i)))
        bin_str = decimal2binary(S)
        for j in range (8):
            RPi.GPIO.output(dac[j], bin_str[j])
        time.sleep(0.005)
        if RPi.GPIO.input(comp) == 0:
            S = int(S - pow(2, (7-i)))
    return S + 5

def led(value):
    RPi.GPIO.output(leds, 0)
    for j in range (8):
        if value > 32 * (j + 1):
            RPi.GPIO.output(leds[j], 1)
    time.sleep(0.2)
    return 0

try:
    while True:
        dec = adc()
        print(dec, dec/256*3.3)
        led(dec)
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.output(troyka, 0)
    RPi.GPIO.cleanup()
        