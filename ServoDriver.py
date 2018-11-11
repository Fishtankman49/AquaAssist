import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

pwm=GPIO.PWM(7,250)
pwm.start(50)

print("Starting FEEDING")

try:
    pwm.ChangeDutyCycle(2)
    time.sleep(2)
    for i in range (0,95):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.05)
    pwm.stop()
    GPIO.cleanup()
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

    
