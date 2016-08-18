####################
# Playback (audio)
#
# 2015-01-03
#
# M. Nijenstein
####################

import RPi.GPIO as GPIO
import pygame.mixer as mixer
import wave
import time

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="playback FILE", metavar="FILE")
parser.add_option("-s", "--start_pos", dest="starting_position",
                  type="float", default=0.0,
                  help="start at STARTPOS ms", metavar="STARTPOS")

(options, args) = parser.parse_args()

#Header
print("*" * 20)
print("Playback")
print("*" * 20)

GPIO.setmode(GPIO.BCM)

#Define ports
play_pause_switch = 24
rewind_switch = 22
extra_switch = 23

#Initialize ports
GPIO.setup(play_pause_switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(rewind_switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(extra_switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Get sample rate
#wavFile = wave.open('Wim1.wav')
#framerate = wavFile.getframerate()
#print("Framerate: %i" % framerate)
#mixer.pre_init(frequency=framerate, size=-16)

mixer.init()
#mixer.music.load('Wim1.wav')

mixer.music.load(options.filename)

rewind_step = 3000
start_position = options.starting_position
position_s = start_position*0.001
mixer.music.play(0, position_s)
mixer.music.pause()
mixer.music.set_volume(1.0)

playing = False
rewound = False

try:
    while True:
        if GPIO.input(play_pause_switch) == True:
            if not playing:
                if rewound:
                    rewound = False
                    print("resume from: %.0f ms" % position)
                    start_position=position
                    position_s = start_position*0.001
                    mixer.music.play(0,position_s)
                else:
                    print("unpause")
                    mixer.music.unpause()
                playing = True
        else:
            if playing:
                print("pause")
                mixer.music.pause()
                playing = False
                position = mixer.music.get_pos()+start_position
            else:
                if GPIO.input(rewind_switch) == True:
                    print("rewind")
                    mixer.music.stop()
                    if position > rewind_step:
                        position = position - rewind_step
                        print("position: %.0f ms" % position)
                        rewound = True
                    else:
                        position = 0.0
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
except:
    print("Error")
finally:
    print("Exiting")
    GPIO.cleanup()
