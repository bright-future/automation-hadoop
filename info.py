#!/usr/bin/python
import re
import os
import sys
fh=open("/root/Desktop/project/ips.txt","r")
for i in fh.readlines():
	os.system("sshpass -p 'redhat' ssh  -o  \"StrictHostKeyChecking no\"  root@"+i.strip()+" ' lscpu |grep -w ^CPU|grep -v op|grep -v f '>>/root/Desktop/project/baba/"+i.strip())
	os.system("sshpass -p 'redhat' ssh  root@"+i.strip()+" ' free -m |grep Mem '>>/root/Desktop/project/baba/"+i.strip())
	os.system("sshpass -p 'redhat' ssh  root@"+i.strip()+" '  df -Th|grep -w \"/\" ' >>/root/Desktop/project/baba/"+i.strip())


