#!/usr/bin/env python

import time
import picamera
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)


while True:
    if (GPIO.input(23) == False):
        print 'Taking photo'
	date_string = time.strftime("%Y-%m-%d-%H:%M:%S")
	with picamera.PiCamera() as camera:
		camera.capture('image' + date_string + '.jpg');
        time.sleep(1)
    if (GPIO.input(24) == False):
        print 'shutdown now!'
	os.system("sudo shutdown -h now")

time.sleep(1)
GPIO.cleanup()
