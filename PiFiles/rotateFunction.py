
from smbus import SMBus
import time
import pwm0 as pwm

<<<<<<< Updated upstream
=======
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


>>>>>>> Stashed changes
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
<<<<<<< Updated upstream



	b = SMBus(1)
	L3G = 0x6b
	who = 0b11010111

	Z_MSB = 0x2d
	Z_LSB = 0x2c

	CTRL_GYRO_1 = 0x20
	CTRL_GYRO_2 = 0x21 
	CTRL_GYRO_6 = 0x39 

	b.write_byte_data(L3G, CTRL_GYRO_1, 0b00001111)
	b.write_byte_data(L3G, CTRL_GYRO_2, 0x00)
	b.write_byte_data(L3G, CTRL_GYRO_6, 0b000000)

	sens = .00875

=======
	global ready
>>>>>>> Stashed changes
	value2 = True
	while value2:
<<<<<<< Updated upstream
    		start = time.time()
    		z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB))
    		zdps = z*sens
    		heading = zdps *time_div(start)
    		angle += heading
    		print(angle)
		
		if value1 > 0:
			if(abs(angle) >=  360):
        			angle = 0
    			if angle <  value1:
        		 	pwm.lspin()
    			else:
         			pwm.stop()
				value2 = False
		elif value1 < 0:
			if(abs(angle) >=  360):
                        	angle = 0
                	if angle >  value1:
                         	pwm.rspin()
                	else:
                        	pwm.stop()
				value2 = False


#while  True:
#    start = time.time()
#    z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB))
#    zdps = z*sens
#    heading = zdps *time_div(start)
#    angle += heading
#    print(angle)
=======
		ready = b.read_byte_data(L3G, CTRL_DRDY) #check if new data is ready
		if(ready and 0b00000100 == 0b00000100): #run when new z data is ready
			div = time_div(start) #time between samples
			start = time.time() #sample end time = sample begin time for next sample
    		z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB)) #take sample
    		zdps = z*sens #adjust for sensitivity rating
    		angle += zdps*div #add data to recorded angle
    		print(angle)

			if(abs(angle) >= 360): #reset angle after one rotation
				angle = 0
			
			if value1 > 0:
    			if angle <  value1:
        	 		pwm.lspin()
    			else:
     				pwm.stop()
				value2 = False
			
			elif value1 < 0:
                if angle >  value1:
                 		pwm.rspin()
        		else:
					pwm.stop()
				value2 = False
				
		ready = b.read_byte_data(L3G, CTRL_DRDY) #check for newe data
>>>>>>> Stashed changes
