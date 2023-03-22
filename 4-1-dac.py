import RPi.GPIO

def decimal2binary(value):

    return [int(bit) for bit in bin(value)[2:].zfill(8)]

RPi.GPIO.setmode(RPi.GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

RPi.GPIO.setup(dac, RPi.GPIO.OUT)

try:
    while True:
        s = input("Enter a number from 0 to 255: ")
        if s == 'q':
            break
        elif ((int(s)>256) or (int(s)<0)):
            print("ERROR: Number is outside of the avaible values")
        else:
            dec = int(s)
            bin_str = decimal2binary(dec)
            for i in range (8):
                RPi.GPIO.output(dac[i], bin_str[i])
        print(3.3 * dec / 256)
finally:
    RPi.GPIO.output(dac, 0)
    RPi.GPIO.cleanup()