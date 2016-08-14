####################
# PiPortControl
#
# 2016-07-20
#
# M. Nijenstein
####################

import piPortInterface as ppi
import time

print("*" * 20)
print("PiPortControl")
print("*" * 20)

pc = ppi.PiPortInterface()
pc.readAllPorts()

#pc.allOn()
#pc.portOn(40)

pc.portOn(36)#b
pc.portOn(37)#g
pc.portOn(38)#r

time.sleep(3)
pc.portOff(36)
time.sleep(1)
pc.portOn(36)

pc.portOff(37)
time.sleep(1)
pc.portOn(37)

pc.portOff(38)
time.sleep(1)
pc.portOn(38)

#pc.readAllPorts()
#time.sleep(10)
pc.allOff()
pc.readAllPorts()

print("Exiting")
