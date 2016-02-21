#!/usr/bin/python2 
import os
import operator
import sys

cpuno=0
processor=0
freeram=0
freehd=0
total=0;
ram={}
hd={}
sequence={}
seq={}
status={}
#updatedip=[]
count=int(1)
def set_manual():
	fa=open("ips.txt","r")
	for j in fa.readlines():
		fh=open("baba/"+j.strip(),"r")
		c=0
		global count
		#global count,ram,hd,sequence,seq,status
		for i in fh.readlines():
			i=i.split()
			if c==0:
				cpuno=int(i[1])
				#print i[1]
				if(cpuno<=1):
					#os.system("rm -rf /root/Desktop/project/baba/"+j)
					break
			
			elif c==1:
				processor=float(i[2])
				#print i[2]
				if(processor<=1000.000):
					#os.system("rm -rf /root/Desktop/project/baba/"+j)
					break
			
			elif c==2:
				freeram=int(i[3])
				j=str(j.strip())
				#print j
				ram[j]=freeram
				#print i[3]
			elif c==3:
				x=i[3]
				x=x[0:-1]
				freehd=float(x)
				j=j.strip()
				hd[j]=freehd
				#print i[3] 
			c=c+1
		
		if c==4:
			j=j.strip()
			sequence[j]=count
			seq[count]=j
			status[j]=0
			count+=1
		fh.close()
#set_manual()
#print(ram)
#print(hd)
#print(sequence)
#print(status)
string=[]
def form_string(): 
	global string	
	for i in range(1,count):
		#string[i-1]=str(str(seq[i])+" "+str(sequence[seq[i]])+"   "+str(ram[seq[i]])+"   "+str(hd[seq[i]]))
		string.append(str(str(sequence[seq[i]])+"   "+str(seq[i])+"   "+str(ram[seq[i]])+"   "+str(hd[seq[i]])))
		#print(i)
		#print(string[i-1])
#form_string()
#print(string)

def display():
	print ("Ip	      Id\t\tFree_Ram\t\tFree_Hardisk\t\tStatus")
	for i in range(1,count):
		#print(seq[i]+"   "+sequence[seq[i]]+"   "+ram[seq[i]]+"   "+hd[seq[i]])
		sys.stdout.write(str(seq[i]))
		sys.stdout.write("    ")
		sys.stdout.write(str(sequence[seq[i]]))
		sys.stdout.write("\t\t")
		sys.stdout.write(str(ram[seq[i]]))
		sys.stdout.write("\t\t\t")
		sys.stdout.write(str(hd[seq[i]]))
		sys.stdout.write("\t\t\t")
		if status[seq[i]]==0:
			print("none")
		elif status[seq[i]]==1 :
			print("namenode")
		elif status[seq[i]]==2 :
			print("jobtracker")
		elif status[seq[i]]==3 :
			print("datanode")
		elif status[seq[i]]==4 :
			print("tasktracker")
		elif status[seq[i]]==5 :
			print("datanode,tasktracker")

#display()
def set_namenodeANDjobtracker(idofnn,idofjt):
	#idofnn=int(raw_input("enter  Id for name node  "))
	status[seq[idofnn]]=1
	#idoftt=int(raw_input("enter  Id for task tracker  "))
	status[seq[idofjt]]=2
	ft=open("/root/Desktop/project/task.txt","w")
	ft.write(seq[idofnn])
	ft.write("\n")
	ft.write(seq[idofjt])
	ft.write("\n")
	ft.close()
"""
while (True):
	print(" -->Enter following commands for Ips\n -->'p' for print\n -->'a' for assining\n -->'r' removing\n -->'w' for write/confirmation")
	command=raw_input("Enter Command  ")
	if command=='p':
		display()
	elif command=='a':
		a=int(raw_input("enter 3 for datanode \n 4 for tasktracker\n\n"))
		x=raw_input("enter the Id's giving spaces eg- 1 4 6\n")
		x=x.split()
		for i in range(0,len(x)):
			if x[i]==idofnn or x[i]==idoftt:
				print("operation not allowed for Id="+x[i])
			elif a==3 and status[seq[int(x[i])]]==0:
				status[seq[int(x[i])]]=3
			elif a==4 and status[seq[int(x[i])]]==0:
				status[seq[int(x[i])]]=4
			elif a==4 and status[seq[int(x[i])]]==3:
				status[seq[int(x[i])]]=5
			elif a==3 and status[seq[int(x[i])]]==4:
				status[seq[int(x[i])]]=5
			
	elif command=='r':
		a=int(raw_input("enter 3 for datanode \n 4 for tasktracker   "))
		x=raw_input("enter the Id's giving spaces eg- 1 4 6   ")
		x=x.split()
		for i in range(0,len(x)):
			if x[i]==idofnn or x[i]==idoftt:
				print("operation not allowed for Id= "+x[i])
			elif a==0 and status[seq[int(x[i])]]==3:
				status[seq[int(x[i])]]=0
			elif a==0 and status[seq[int(x[i])]]==4:
				status[seq[int(x[i])]]=0
			elif a==4 and status[seq[int(x[i])]]==5:
				status[seq[int(x[i])]]=3
			elif a==3 and status[seq[int(x[i])]]==5:
				status[seq[int(x[i])]]=4
		
	elif command=='w':
		break
"""
#display()
def set_tasktracer_and_datanode():
	ft=open("task.txt","a")
	fd=open("hd.txt","a")

	for i in range(1,count):
		if status[seq[i]]==5:
			ft.write(seq[i])
			fd.write(seq[i])
			ft.write("\n")
			fd.write("\n")
		elif status[seq[i]]==3:
			fd.write(seq[i])
			fd.write("\n")
		elif status[seq[i]]==4:
			ft.write(seq[i])
			ft.write("\n")

	ft.close()
	fd.close()

		




