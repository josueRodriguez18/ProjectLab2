import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

refreshRate = 1
counterR = 0
counterL = 0
IO.add_event_detect(14, IO.BOTH)
IO.add_event_detect(15, IO.BOTH)
while True:
	L0 = IO.event_detected(14)
	R0 = IO.event_detected(15)
	if L0:
		L0=False
		counterL = counterL + 1
	if counterL>=refreshRate:
		#turn off left motor
	if R0:
		R0=False
		counterR = counterR + 1
	if counterR>=refreshRate:
		#turn off right motor
	if counterL>=refreshRate and counterR>=refreshRate:
		counterL = 0
		counterR = 0
		#turn on left motor
		#turn on right motor
