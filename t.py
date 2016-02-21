#!/usr/bin/python 
import re
import os
import glob 
fa=open("/root/Desktop/folder/ip.txt","r")
for j in fa.readlines():
	fh=open("/root/Desktop/baba/"+j.strip(),"r")
	os.system("touch /root/Desktop/daba/"+j)
	fo=open("/root/Desktop/daba/"+j,"a")    
	for i in fh.readlines():
		i=i.strip()
		x=re.sub(' +',' ',i)
		fo.write(x)
		fo.write("\n")
	fo.close()
	fh.close()

