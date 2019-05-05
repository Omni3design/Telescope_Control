"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import adafruit_motorkit
import adafruit_motor
import time

kit = MotorKit()

kit.stepper1.release()

print("Single Step")
for i in range(200):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    #print(i)
kit.stepper1.release()
time.sleep(5)

print("Double Step")
for j in range(200):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
kit.stepper1.release()
time.sleep(5)
#print("Interleave Step")
#for k in range(200):
#    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVED)
#release()
#time.sleep(5)
print("Microstep")
for l in range(200):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
kit.stepper1.release()
time.sleep(5)
