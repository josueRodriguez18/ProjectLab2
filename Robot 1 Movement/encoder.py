import RPi.GPIO as IO
import time

#Motor A is the Left Motor
#Motor B is the Right Motor

#Set I/O
IO.setwarnings(False)
IO.setmode(IO.BOARD)

#Motor Control Pins
IO.setup(11, IO.OUT)    #ENA
IO.setup(13, IO.OUT)    #IN1
IO.setup(15, IO.OUT)    #IN2
IO.setup(19, IO.OUT)    #ENB
IO.setup(21, IO.OUT)    #IN3
IO.setup(23, IO.OUT)    #IN4

#Photointerrupter Pins
IO.setup(8, IO.OUT)	#Photointerrupter Motor A Vcc
IO.setup(10, IO.IN)	#Photointerrupter Motor A signal
IO.setup(12, IO.OUT)	#Photointerrupter Motor A Gnd
IO.setup(22, IO.OUT)	#Photointerrupter Motor B Vcc
IO.setup(24, IO.IN)	#Photointerrupter Motor B signal
IO.setup(26, IO.OUT)	#Photointerrupter Motor B Gnd

#Add event listener to Photointerrupter Pins
IO.add_event_detect(10, IO.BOTH) #Motor A signal
IO.add_event_detect(24, IO.BOTH) #Motor B signal

#Set PWMs for Motors
pwma = IO.PWM(11, 100) #setup pwm on ENA pin 11 freq. 100hz
pwmb = IO.PWM(19, 100) #setup pwm on ENB pin 19 freq. 100hz
pwma.start(0) #start ENA duty cycle at 0%
pwmb.start(0) #start ENB duty cycle at 0%

#Turn on Photointerrupters
IO.output(8, True)
IO.output(12, False)
IO.output(22, True)
IO.output(26, False)

#Forward
def forward(value1):
    pwma.ChangeDutyCycle(90)    #90% duty cycle on motor a
    pwmb.ChangeDutyCycle(90)    #90% duty cycle on motor b
    IO.output(13, False)        #IN1 motor a
    IO.output(15, True)         #IN2 motor a
    IO.output(21, True)         #IN3 motor b
    IO.output(23, False)        #IN4 motor b
    x = 0
    refreshRate = 1 #40 divided by refresh rate = refreshes per rotation
    counterR = 0 #Should always start at 0
    counterL = 0 #Should always start at 0
    while x < value1:
	L0 = IO.event_detected(10) #Sets variable to if an edge is detected
	R0 = IO.event_detected(24) #Sets variable to if an edge is detected
	if L0:
		L0=False #Edge detected
		counterL = counterL + 1 #Increment counter
	if counterL>=refreshRate:
		IO.output(15, False) #turn off motor a
	if R0:
		R0=False #Edge detected
		counterR = counterR + 1 #Increment counter
	if counterR>=refreshRate:
		IO.output(21, False) #turn off motor b
	if counterL>=refreshRate and counterR>=refreshRate:
		counterL = 0 #Reset counter
		counterR = 0 #Reset counter
		IO.output(15, True) #turn on motor a
		IO.output(21, True) #turn on motor b
	x = x+0.00005
