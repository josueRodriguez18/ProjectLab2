from smbus import SMBus
import threading
import Queue
import RPi.GPIO as IO
import time

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
angle = [0]
start = time.time()
b = SMBus(1)
who = 0b11010111

Z_MSB = 0x2d
Z_LSB = 0x2c

CTRL_GYRO_1 = 0x20
CTRL_GYRO_2 = 0x21
CTRL_GYRO_6 = 0x39
CTRL_DRDY = 0x27
L3G = 0x6b

b.write_byte_data(L3G, CTRL_GYRO_1, 0b00001100)
b.write_byte_data(L3G, CTRL_GYRO_2, 0x00)
b.write_byte_data(L3G, CTRL_GYRO_6, 0b000000)
sens = .00875
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
	getGyro(angle)
	original = angle[0]
	x = 0
	default_right = 90
	default_left = 90
	while x < duration:
		getGyro(angle)
		if abs(angle[0]) < abs(original) + 1 and abs(angle[0]) > abs(original) - 1:
			pwma.ChangeDutyCycle(90)    #90% duty cycl
			pwmb.ChangeDutyCycle(90)    #90% duty cycle
			IO.output(13, False)        #IN1
			IO.output(15, True)         #IN2
			IO.output(21, True)         #IN3
			IO.output(23, False)        #IN4
			print('no drift')
			x = x + 100

		elif getGyro(angle)  > 0:
			if default_right > 10:
				default_right  = default_right - 1
			pwma.ChangeDutyCycle(90)
			pwmb.ChangeDutyCycle(default_right)
			IO.output(13, False)
			IO.output(15, True)
			IO.output(21, True)
			IO.output(23, False)
			print('drift left')
			x = x + 100

		elif getGyro(angle)  < 0:
			if default_left > 10:
				default_left = default_left  - 2
			pwma.ChangeDutyCycle(default_left)
			pwmb.ChangeDutyCycle(90)
			IO.output(13, False)
			IO.output(15, True)
			IO.output(21, True)
			IO.output(23, False)
			print('drift right')
			x = x + 100
		x = x+10000

def stop():
	pwma.ChangeDutyCycle(0)     #0% duty cycle
	pwmb.ChangeDutyCycle(0)     #0% duty cycle
	IO.output(13, False)        #IN1
	IO.output(15, False)        #IN2
	IO.output(21, False)        #IN3
	IO.output(23, False)        #IN4

def forward_right():
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(90)
		pwmb.ChangeDutyCycle(25)
		IO.output(13, True)
		IO.output(15, False)
		IO.output(21, False)
		IO.output(23, True)
		x = x+1

def forward_left():
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(25)
		pwmb.ChangeDutyCycle(90)
		IO.output(13, True)
		IO.output(15, False)
		IO.output(21, False)
		IO.output(23, True)
		x = x+1

def lspin():
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(45)
		pwmb.ChangeDutyCycle(45)
		IO.output(13, True)         #IN1
		IO.output(15, False)        #IN2
		IO.output(21, True)	    #IN3
		IO.output(23, False)        #IN4
#	final = final - 50
#	while angle[0]  < final:
#		getGyro(angle)
#	stop()

def rspin(): #current angle, desired angle
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(45)	#90% duty cycle
		pwmb.ChangeDutyCycle(45)	#90% duty cycle
		IO.output(13, False)		#IN1
		IO.output(15, True)			#IN2
		IO.output(21, False)        #IN3
		IO.output(23, True)         #IN4
	x = x+1

def twos_comp_combine(msb, lsb):
	twos_comp = 256*msb + lsb
	if twos_comp >= 32768:
		return twos_comp - 65536
	else:
		return twos_comp

def time_div(start):
	current = time.time()
	return current - start

def getGyro(angle):
	while True:
		ready = b.read_byte_data(L3G, CTRL_DRDY) #checks to see if there is new Z data ready
		if(ready * 0b0000100 == 0b0000100): #run if new data is ready
			div = time_div(start) #time division between values
			start = time.time() #record time for next sample
			z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB))
			zdps = z*sens
			heading = zdps*div
			angle[0] += heading
			print(angle[0])
		if (abs(angle[0]) >= 360):
			angle[0] = 0
	#print(angle[0])
	return heading
