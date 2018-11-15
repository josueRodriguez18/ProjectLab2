from smbus import SMBus
import time
import pwm0 as pwm

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

	value1 = value1 * 7 / 10

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

	value2 = True
	while value2:
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
