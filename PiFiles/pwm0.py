import RPi.GPIO as IO

#pwm setup
IO.setwarnings(False)   #disable warnings
IO.setmode(IO.BOARD)    #specifies reference to pins on the board

IO.setmode(IO.BOARD)
IO.setup(11, IO.OUT)    #ENA
IO.setup(13, IO.OUT)    #IN1
IO.setup(15, IO.OUT)    #IN2
IO.setup(19, IO.OUT)    #ENB
IO.setup(21, IO.OUT)    #IN3
IO.setup(23, IO.OUT)    #IN4

pwma = IO.PWM(11, 100)  #setup pwm on ENA pin 11 freq. 100hz
pwmb = IO.PWM(19, 100)  #setup pwm on ENB pin 19 freq. 100hz

pwma.start(0)   #ENA duty cycle 0%
pwmb.start(0)   #ENB duty cycle 0%

#gyro setup

#_________7__________________________________________________________________
def backward():
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(90)    #90% duty cycle
		pwmb.ChangeDutyCycle(85)    #90% duty cycle
		IO.output(13, True)         #IN1
		IO.output(15, False)        #IN2
		IO.output(21, False)        #IN3
		IO.output(23, True)         #IN4
		x = x+1

def forward(duration):
	x = 0
	while x < duration:
			pwma.ChangeDutyCycle(90)    #90% duty cycl
			pwmb.ChangeDutyCycle(90)    #90% duty cycle
			IO.output(13, False)        #IN1
			IO.output(15, True)         #IN2
			IO.output(21, True)         #IN3
			IO.output(23, False)        #IN4
			x += 100

def stop():
	pwma.ChangeDutyCycle(0)     #0% duty cycle
	pwmb.ChangeDutyCycle(0)     #0% duty cycle
	IO.output(13, False)        #IN1
	IO.output(15, False)        #IN2
	IO.output(21, False)        #IN3
	IO.output(23, False)        #IN4


def lspin():   #current angle, desired angle
	pwma.ChangeDutyCycle(45)    #90% duty cycle
	pwmb.ChangeDutyCycle(45)    #90% duty cycle
	IO.output(13, True)         #IN1
	IO.output(15, False)        #IN2 
	IO.output(21, True)        #IN3
	IO.output(23, False)         #IN4

def rspin(): #current angle, desired angle
	pwma.ChangeDutyCycle(30)    #90% duty cycle
	pwmb.ChangeDutyCycle(30)    #90% duty cycle
	IO.output(13, False)         #IN1
	IO.output(15, True)        #IN2 
	IO.output(21, False)        #IN3
	IO.output(23, True)         #IN4
