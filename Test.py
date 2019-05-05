from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

# User Inputs
Folder= raw_input('Input Folder Location: ')
Name = raw_input('Input Image Name: ')
Capture_Mode = input('Input Capture Mode (Single[1]/Cont[2]): ')
if Capture_Mode == 1:
	Pic_Num = 1
else:
	Pic_Num = input('Input Number of Pictures: ')

#Make sure Folder path exisits
Folder_Path = ('/home/pi/Photos/'+ Folder + '/')
if not os.path.isdir (Folder_Path):
	os.makedirs(Folder_Path)

Cont = 'Y'
while Cont == 'Y' :
	if Capture_Mode == 1:
		camera.capture(Folder_Path + Name + '.jpg')
	else:
		for i in range (Pic_Num):
			camera.capture((Folder_Path + Name + '{0:04d}.jpg').format(i))
			print('Image Taken')
	Cont = raw_input('Continue Taking Pictures? (Y/N): ')
	if Cont =='Y':
		RepeatF=raw_input('Use Same Folder Location? (Y/N): ')
		if RepeatF == 'N':
			Folder = raw_input('Input Folder Location: ')
			Folder_Path = ('/home/pi/Photos/'+ Folder + '/')
			if not os.path.isdir (Folder_Path):
				os.makedirs(Folder_Path)
		RepeatN = raw_input('Use Same File Name? (Y/N): ')
		if RepeatN == 'N':
			Name = raw_input('Input Image Name: ')
		RepeatM = raw_input('Use same Capture Mode? (Y/N): ')
		if RepeatM == 'N':
			Capture_Mode = input('Input Capture Mode (Single[1]/Cont[2]): ')
			if Capture_Mode == 1:
				Pic_Num = 1
			else:
				Pic_Num = input('Input Number of Pictures: ')
	

