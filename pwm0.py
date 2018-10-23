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
angle = 0
b = SMBus(1)
who = 0b11010111

Z_MSB = 0x2d
Z_LSB = 0x2c

CTRL_GYRO_1 = 0x20
CTRL_GYRO_2 = 0x21
CTRL_GYRO_6 = 0x39
L3G = 0X6b

b.write_byte_data(L3G, CTRL_GYRO_1, 0b00001111)
b.write_byte_data(L3G, CTRL_GYRO_2, 0x00)
b.write_byte_data(L3G, CTRL_GYRO_6, 0b000000)
sens = .00875
queue = Queue.Queue(1)

#___________________________________________________________________________

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
	original = angle
	x = 0
	default = 90
	while x < duration:
		if abs(angle)  < (abs(original) - .5):
			pwma.ChangeDutyCycle(90)    #90% duty cycl
			pwmb.ChangeDutyCycle(90)    #90% duty cycle
			IO.output(13, False)        #IN1
			IO.output(15, True)         #IN2
			IO.output(21, True)         #IN3
			IO.output(23, False)        #IN4
			default = 90
			print('no drift')
			x = x + 1
		elif getGyro()  > 0:
			default  = default - 10
			pwma.ChangeDutyCycle(default)
			pwmb.ChangeDutyCycle(90)
			IO.output(13, False)
			IO.output(15, True)
			IO.output(21, True)
			IO.output(23, False)
			print('drift right')
			queue.get()
			print('still here')
		elif getGyro()  < 0:
			default = default -10
			pwma.ChanceDutyCycle(90)
			pwmb.ChanceDutyCycle(default)
			IO.output(13, False)
			IO.output(15, True)
			IO.output(21, True)
			IO.output(23, False)
			print('drift left')
			x = x + 1
		x = x+1

def stop():
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(0)     #0% duty cycle
		pwmb.ChangeDutyCycle(0)     #0% duty cycle
		IO.output(13, False)        #IN1
		IO.output(15, False)        #IN2
		IO.output(21, False)        #IN3
		IO.output(23, False)        #IN4
		x = x+1

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
		pwma.ChangeDutyCycle(30)    #90% duty cycle
		pwmb.ChangeDutyCycle(30)    #90% duty cycle
		IO.output(13, True)         #IN1
		IO.output(15, False)        #IN2 
		IO.output(21, True)        #IN3
		IO.output(23, False)         #IN4
		x = x+1

def rspin():
	x = 0
	while x < 1:
		pwma.ChangeDutyCycle(30)    #90% duty cycle
		pwmb.ChangeDutyCycle(30)    #90% duty cycle
		IO.output(13, False)         #IN1
		IO.output(15, True)        #IN2 
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

def getGyro(angle, queue):
	start = time.time()
	z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB))
	zdps = z*sens
	heading = zdps*time_div(start)
	if abs(zdps) > .2:
		angle += 3*heading
	if (abs(angle) >= 360):
		angle = 0
	queue.put(heading)


threading.Thread(target = getGyro, args=[angle, queue]).start()
