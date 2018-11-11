import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

pwm=GPIO.PWM(7,250)
pwm.start(50)

print("Starting FEEDING")

try:
    for t in range (1,5):
        print("Starting FEEDING " + str(t))
        pwm.ChangeDutyCycle(2)
        time.sleep(.5)
        for i in range (0,95):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
        pwm.ChangeDutyCycle(2)
        time.sleep(.5)
        time.sleep(10)
    pwm.stop()
    GPIO.cleanup()
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
