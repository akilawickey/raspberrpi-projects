import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
i=1


while 1:
  print "MOTOR on"
  GPIO.output(18,GPIO.HIGH)
  GPIO.output(17,GPIO.LOW)
  time.sleep(4)
  print "MOTOR off"
  GPIO.output(18,GPIO.LOW)
  GPIO.output(17,GPIO.HIGH)
  time.sleep(4)
  i=i+1
  if (i>4):
   break
