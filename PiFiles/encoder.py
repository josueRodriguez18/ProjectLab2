import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BOARD)

L0 = IO.input(14)
R0 = 
counterR = 0
counterL = 0
IO.add_event_detect(14, IO.BOTH)
IO.add_event_detect(15, IO.BOTH)
while True:
	L0 = IO.event_detected(14)
	R0 = IO.event_detected(15)
	if x == 0 & x2 == 1:
		counterL++
		x = x2
	
