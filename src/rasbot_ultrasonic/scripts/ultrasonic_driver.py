#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

class UltrasonicSensor:

    def __init__(self, echo_pin = 24, trigger_pin = 23):
        self.ECHO_PIN = echo_pin
        self.TRIGGER_PIN = trigger_pin
        self._SPEED_SOUND = 343.0

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)

    def read_raw(self):

        GPIO.output(self.TRIGGER_PIN, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIGGER_PIN, False)

        start = time.time()
        while GPIO.input(self.ECHO_PIN) == 0:
            start = time.time()
        stop = time.time()
        while GPIO.input(self.ECHO_PIN) == 1:
            stop = time.time()
            if stop - start >= 0.04:
                stop = start
                break
        out = stop - start
        return out * self._SPEED_SOUND / 2

if __name__ == "__main__":

    sensor = UltrasonicSensor()

    while True:
        print(f"Sensor Reading: {sensor.read()}")
        time.sleep(0.5)