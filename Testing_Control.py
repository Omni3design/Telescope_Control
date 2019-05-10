'Demo Control'
import math
from math import sin
from math import cos
from math import degrees
from math import radians
from math import asin
from math import acos
import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

AzMotor = MotorKit().stepper1
AltMotor = MotorKit().stepper2

AzMotor.release()
AltMotor.release()

'read current time in milli seconds'
current_milli_time = int(time.clock() * 1000)

StartTime = current_milli_time


for i in range (100):
    current_milli_time = int(time.clock() * 1000)
    'print(current_milli_time)'
    CurrentTime = current_milli_time - StartTime
    
    'Read Target Inputs'

    'Read System Inputs'

    'Do Conversion'

    'Set Motor Position'

    'Send Command to Motors'

    'Take Picture'
