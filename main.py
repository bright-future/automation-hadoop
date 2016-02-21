#!/usr/bin/python
import os
os.system("python getip.py")
os.system("python info.py")
while True:
	print("Enter command \n 1.Manual   2.Automatic ")
	a=int(raw_input())
	if a==1:
		os.system("python manual.py")
		break
	elif a==2:
		os.system("python final.py")
		break
	else:
		print("Wrong choice")
os.system("python runconf.py")


