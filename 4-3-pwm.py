import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.OUT)

p = RPi.GPIO.PWM(2, 1000)
p.start(0)

try:
    while True:
        f = int(input("enter your cicle period:"))
        p.ChangeDutyCycle(f)
        print(3.3 * f / 100)
   
finally:
    p.stop()
    RPi.GPIO.output(2, 0)
    RPi.GPIO.cleanup()