#!/usr/bin/python2 
import os
import sys

#namenode
fh=open("/root/Desktop/project/task.txt","r")
nn= fh.readline()
os.system("sshpass -p 'redhat' scp /root/Desktop/project/confnamenode.py  root@"+nn.strip()+":/root/Desktop")
os.system("sshpass -p 'redhat' scp /root/Desktop/project/task.txt  root@"+nn.strip()+":/root/Desktop")
os.system("sshpass -p 'redhat' ssh -o \"StrictHostKeyChecking no\" root@"+nn.strip()+" 'python2 /root/Desktop/confnamenode.py'")

#jobtracer
jt=fh.readline()
os.system("sshpass -p 'redhat' scp /root/Desktop/project/confjobtracer.py  root@"+jt.strip()+":/root/Desktop")
os.system("sshpass -p 'redhat' scp /root/Desktop/project/task.txt  root@"+jt.strip()+":/root/Desktop")
os.system("sshpass -p 'redhat' ssh -o \"StrictHostKeyChecking no\" root@"+jt.strip()+" 'python2 /root/Desktop/confjobtracer.py'")

#tasktracer
for i in fh.readlines():
	os.system("sshpass -p 'redhat' scp /root/Desktop/project/conftasktracer.py  root@"+i.strip()+":/root/Desktop")
	os.system("sshpass -p 'redhat' scp /root/Desktop/project/task.txt  root@"+i.strip()+":/root/Desktop")
	os.system("sshpass -p 'redhat' ssh -o \"StrictHostKeyChecking no\" root@"+i.strip()+" 'python2 /root/Desktop/conftasktracer.py'")

fh.close()

#datanode
fh=open("/root/Desktop/project/hd.txt","r")
for i in fh.readlines():
	if i==nn or i==jt:
		continue
	os.system("sshpass -p 'redhat' scp /root/Desktop/project/confdatanode.py root@"+i.strip()+":/root/Desktop")
	os.system("sshpass -p 'redhat' scp /root/Desktop/project/task.txt  root@"+i.strip()+":/root/Desktop")
	os.system("sshpass -p 'redhat' ssh -o \"StrictHostKeyChecking no\" root@"+i.strip()+" 'python2 /root/Desktop/confdatanode.py'")



