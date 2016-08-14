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
pc.portOn(36)#b
pc.portOn(37)#g
pc.portOn(38)#r

print("Press crtl-c to quit...")

try:
    while True:
        offset = 8
        site = urllib2.urlopen('http://sites.google.com/site/pellesteinweb/pi')
        contents = site.read()
        value_at = contents.find('waarde')
        value = contents[value_at+offset]

        if value == "1":
            pc.portOn(37)
            pc.portOff(38)
        else:
            pc.portOn(38)
            pc.portOff(37)
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
