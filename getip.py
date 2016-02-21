#!usr/bin/python

import os
import sys
os.system("yum install sshpass -y")
os.system("yum install nmap -y")
os.system("nmap 192.168.0.0/24 -oG /root/Desktop/project/ip1.txt")
os.system('cat  /root/Desktop/project/ip1.txt|grep ssh|grep open|cut -f2 -d " ">/root/Desktop/project/ips.txt')
os.system("mkdir /root/Desktop/project/baba")
