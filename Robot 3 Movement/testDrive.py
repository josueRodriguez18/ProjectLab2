#import pdb
import encoder as str8
import rotateFunction as rotate
import pwm0 as pwm
import time
import sys

while True:
	str8.forward(10)
	pwm.stop()
	time.sleep(1)
	rotate.rotate(180)
	pwm.stop()
	time.sleep(1)
	str8.forward(10)
	pwm.stop()
	time.sleep(1)
	rotate.rotate(-180)
	pwm.stop()
	time.sleep(1)
