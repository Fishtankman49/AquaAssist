import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

pwm=GPIO.PWM(7,50)
pwm.start(50)

print("Starting FEEDING")

pwm.ChangeDutyCycle(8)
time.sleep(1)

pwm.ChangeDutyCycle(150)
time.sleep(3)

pwm.stop()
GPIO.cleanup()
