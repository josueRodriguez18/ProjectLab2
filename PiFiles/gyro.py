import RPi.GPIO as GPIO
import spidev

#SDI pins used
SCL = 14
MOSI = 12
MISO = 13
CS = 0

#Z output registers
Z_MSB = 0xAD
Z_LSB = 0XAC


#pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SCL, GPIO.OUT)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(MISO, GPIO.IN)
GPIO.setup(CS,  GPIO.OUT)

#create spidev object and open bus
spi = spidev.SpiDev()
spi.open(0, 0) #bus 0 device 0
#set max speed
spi.max_speed_hz = 5000

while True:
    #release chip select
    GPIO.output(CS, 0)
    #begin transfers
    temp = spi.xfer(Z_MSB, 5000, 0, 8)
    GPIO.output(CS, 1)
    input()







