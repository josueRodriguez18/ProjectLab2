from smbus import SMBus
import time
import pwm0 as pwm

b = SMBus(1)
L3G = 0x6b
who = 0b11010111
Z_MSB = 0x2d
Z_LSB = 0x2c

CTRL_GYRO_1 = 0x20
CTRL_GYRO_2 = 0x21
CTRL_GYRO_6 = 0x39
CTRL_DRDY = 0x27

b.write_byte_data(L3G, CTRL_GYRO_1, 0b00001100)
b.write_byte_data(L3G, CTRL_GYRO_2, 0x00)
b.write_byte_data(L3G, CTRL_GYRO_6, 0b000000)
sens = .00875
start = time.time()


def twos_comp_combine(msb, lsb):
        twos_comp = 256*msb + lsb
        if twos_comp >= 32768:
            return twos_comp - 65536
        else:
            return twos_comp

def time_div(start):
    current = time.time()
    return current - start

def rotate(value1):
	angle = 0
	value2 = True
	turnVal = "right"
	global start
	start = time.time()
	while value2:
		angle += sample()
    		print(angle)

		if(abs(angle) >= 360):
			angle = 0

		if value1 > 0:
    			if angle <  value1:
				angle += sample()
        		 	pwm.lspin()
				turnVal = "left"
				angle += sample()
    			else:
         			pwm.stop()
				value2 = False
				angle += sample()
		elif value1 < 0:
                	if angle >  value1:
				angle += sample()
				pwm.rspin()
				turnVal = "right"
				angle += sample()
                	else:
                        	pwm.stop()
				value2 = False
				angle += sample()

	angle += sample()
	while not((abs(angle) > abs(value1) - .5) & (abs(angle) < abs(value1) + .5)) :
		angle += sample()
		print(angle)
		if(turnVal == "right"):
			angle += sample()
			pwm.lspin()
			angle += sample()
		else:
			angle += sample()
			pwm.rspin()
			angle += sample()

	pwm.stop()

def sample():
	global ready
	global start
	ready = b.read_byte_data(L3G, CTRL_DRDY)
	if(ready & 0b00000100 == 0b00000100):
		div = time_div(start)
		start = time.time()
		z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB))
		zdps = z*sens
		return zdps*div
	else:
		return 0
