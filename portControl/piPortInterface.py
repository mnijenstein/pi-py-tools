####################
# PiPortInterface
#
# 2016-07-29
#
# M. Nijenstein
####################

import RPi.GPIO as GPIO
import time

class PiPortInterface:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.ports = [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40]
        for port in self.ports:
            GPIO.setup(port, GPIO.OUT)
            self.portOff(port)

    def portOff(self, port):
        GPIO.output(port, False)

    def portOn(self, port):
        GPIO.output(port, True)

    def portToggle(self, port):
        if self.isOn(port):
            self.portOff(port)
        else:
            self.portOn(port)

    def isOn(self, port):
        return (GPIO.input(port))

    def allPortsOff(self):
        for port in self.ports:
            self.portOff(port)

    def readAllPorts(self):
        for port in self.ports:
            print "%d: %r" % (port, self.isOn(port))

    def cleanup(self):
        GPIO.cleanup()

    def exit(self):
        self.cleanup()
