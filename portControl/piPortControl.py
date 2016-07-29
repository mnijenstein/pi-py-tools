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
pc.portOn(7)
pc.readAllPorts()

#except KeyboardInterrupt:
#    print("KeyboardInterrupt")
#except:
#    print("Error")
#finally:
print("Exiting")
