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

#initial constants
PositionPreviousMilli = 0
PositionRate = 1000

input = 0
	if input == 1:
		print("Input Target RA in hours")
		RA_hour = input()
		print("Input Target DEC in degrees")
		DEC = input()
	else:
		RA_hour = 16.695
		DEC = 36.466667

GPS = 0
if GPS == 1:
	lat = 0
	long = 0
else:
	lat = 52.5
	long =-1.9166667


for i in range (100):
    current_milli_time = int(time.clock() * 1000)
    'print(current_milli_time)'
    CurrentTime = current_milli_time - StartTime
    
    'Read Target Inputs'
	
    'Read System Inputs'
	
	'update current date/time'
	if (CurrentTime - PositionRate) >= PositionPreviousMilli:
		ts = time.gmtime()
		month = int(time.strftime("%m",ts))
		day = int(time.strftime("%d",ts))
		year = int(time.strftime("%Y",ts))
		hour = int(time.strftime("%H",ts))
		minute = int(time.strftime("%M",ts))/60
		sec = int(time.strftime("%S",ts))/3600
		'Do Conversion'
		Time = hour+minute+sec
		RA_DEG = RA_hour*15
		#DEC/RAD Conversions
		RA_RAD = radians(RA_DEG)
		DEC_RAD = radians(DEC)
		Lat_RAD = radians(lat)
		Long_RAD = radians(long)

		#Leap Year Check
		if (year % 4) == 0:
			if (year % 100) == 0:
				if (year % 400) == 0:
					leap_year = True
				else:
					leap_year = False
			else:
				leap_year = True
		else:
			leap_year = False

		#Tables
		if leap_year == False:
			TableA = (0,31,59,90,120,151,181,212,243,273,304,334)
		else:
			TableA = (0,31,60,91,121,152,182,213,244,274,305,335)

		TableB = {
			'2018':6573.5,
			'2019':6938.5,
			'2020':7303.5,
			'2021':7669.5}
			
		day_dec = Time/24

		d = TableA[month-1] + day + day_dec + TableB[str(year)]

		#LST CALC
		LST = 100.46+.985647*d+long+15*Time
		if LST > 360:
			LST_reduced = LST - (360*(LST // 360))

		# Solve Hour Angle from RA (HA)
		HA = LST_reduced - RA_DEG
		if HA < 0:
			HA = HA + 360

		HA_RAD = radians(HA)
		print(HA)
		# Convert HA/Dec to ALT/AZ

		#ALT
		ALT_RAD = asin(sin(DEC_RAD)*sin(Lat_RAD)+cos(DEC_RAD)*cos(Lat_RAD)*cos(HA_RAD))
		ALT = degrees(ALT_RAD)

		#DEC
		DEC_RAD = acos((sin(DEC_RAD)-sin(ALT_RAD)*sin(Lat_RAD))/(cos(ALT_RAD)*cos(Lat_RAD)))
		if sin(HA_RAD)>0:
			DEC = 360 - degrees(DEC_RAD)
		else:
			DEC = degrees(DEC_RAD)

    'Set Motor Position'
	if Alt_Error > .5:
		AltMotorCmd = ALT
	if AZ_Error > .5:
		AzMotorCmd = AZ
	
    'Send Command to Motors'
	
	
    'Take Picture'
