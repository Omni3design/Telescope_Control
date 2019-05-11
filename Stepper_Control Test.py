import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

TestMotor = MotorKit().stepper1

TestMotor.release()

CurrentPos = 0

for i in range(10):
	PosReq = input("Stepper Angle Position:")
	Err = abs(CurrentPos - PosReq) #Degress need to move
	if (CurrentPos - PosReq) > 1:
		Dir = FORWARD
	elif (CurrentPos - PosReq) <1:
		Dir = REVERSE
	
	Steps = Err // 1.8
	#Stepper is 200steps/rev or 1step = 1.8 deg
	for j in range(Steps):
		TestMotor.onestep(direction=stepper.Dir, style=stepper.DOUBLE)