import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

pwm=GPIO.PWM(7,250)
pwm.start(50)

print("Starting FEEDING")

pwm.ChangeDutyCycle(20)
time.sleep(1)

pwm.ChangeDutyCycle(95)
time.sleep(1)

pwm.ChangeDutyCycle(20)
time.sleep(1)

pwm.stop()
GPIO.cleanup()
