from smbus import SMBus
import time
import pwm0 as pwm

#setup I2C communication with gyro
b = SMBus(1)
L3G = 0x6b
who = 0b11010111
#z axis output registers
Z_MSB = 0x2d
Z_LSB = 0x2c

CTRL_GYRO_1 = 0x20
CTRL_GYRO_2 = 0x21
CTRL_GYRO_6 = 0x39
#data ready register
CTRL_DRDY = 0x27

b.write_byte_data(L3G, CTRL_GYRO_1, 0b00001100)
b.write_byte_data(L3G, CTRL_GYRO_2, 0x00)
b.write_byte_data(L3G, CTRL_GYRO_6, 0b000000)
sens = .00875
#take time sample
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
	direction = "right"
	angle = 0
	global ready
	value2 = True
	global start
	start = time.time()
	while value2:
		angle += sample() #add data to recorded angle
		print(angle)

		if(abs(angle) >= 360): #reset angle after one rotation
			angle = 0
			
		if value1 > 0:
			direction = "left"
			if angle <  value1:
       	 		pwm.lspin()
   			else:
   				pwm.stop()
				angle += sample()
			value2 = False
			
		elif value1 < 0:
			direction = "right"
            if angle >  value1:
         		pwm.rspin()
    		else:
				pwm.stop()
				angle += sample()
			value2 = False
		
		#correction
		while not((abs(angle) > abs(value1) - 1) and (abs(angle) < abs(angle) + 1)): #if the current angle isn't within one degree of the desired angle
			angle += sample()
			if(direction == "right"):
				pwm.lspin()
			else:
				pwm.rspin()
		pwm.stop()

def sample():
	global ready
	global start

	ready = b.read_byte_data(L3G, CTRL_DRDY) #check if new data is ready
		if(ready and 0b00000100 == 0b00000100): #run when new z data is ready
			div = time_div(start) #time between samples
			start = time.time() #sample end time = sample begin time for next sample
    		z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB)) #take sample
    		zdps = z*sens #adjust for sensitivity rating
    		return zdps*div #add data to recorded angle
		else:
			return 0