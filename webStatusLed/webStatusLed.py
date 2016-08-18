####################
# WebStatusLed
#
# 2016-07-21
#
# M. Nijenstein
####################

import piPortInterface as ppi
import time
import urllib2
import sys

print("*" * 20)
print("WebStatusLed")
print("*" * 20)

pc = ppi.PiPortInterface()
red = 36
blue = 38
green = 40

pc.portOn(blue)
pc.portOn(green)
pc.portOn(red)

print("Press crtl-c to quit...")

try:
    while True:
        offset = 8
        site = urllib2.urlopen('http://sites.google.com/site/pellesteinweb/pi')
        contents = site.read()
        value_at = contents.find('waarde')
        value = contents[value_at+offset]

        if value == "0":
            pc.portOn(red)
            pc.portOn(blue)
            pc.portOff(green)
        elif value == "1":
            pc.portOn(green)
            pc.portOn(blue)
            pc.portOff(red)
        elif value == "2":
            pc.portOn(red)
            pc.portOn(green)
            pc.portOff(blue)
        else:
            pc.portOn(blue)
            pc.portOn(green)
            pc.portOn(red)
        time.sleep(5)

except KeyboardInterrupt:
    print("KeyboardInterrupt")
except:
    print("Error:")
    e = sys.exc_info()[0]
    print e
finally:
    print("Exiting")
    pc.allOff()
    pc.cleanup()
