from smbus import SMBus
import time

def twos_comp_combine(msb, lsb):
        twos_comp = 256*msb + lsb
        if twos_comp >= 32768:
            return twos_comp - 65536
        else:
            return twos_comp

def time_div(start):
    current = time.time()
    return current - start

angle = 0



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

while True:
    start = time.time()
    z = twos_comp_combine(b.read_byte_data(L3G, Z_MSB), b.read_byte_data(L3G, Z_LSB))
    zdps = z*sens
    heading = zdps *time_div(start)
    if(abs(zdps) > .35):
            angle += heading
    print(angle)
    if(abs(angle) == 360):
            angle = 0
