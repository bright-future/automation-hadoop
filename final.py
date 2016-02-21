#!/usr/bin/python2 
import os
import operator
cpuno=0
processor=0
freeram=0
freehd=0
total=0;
ram={}
hd={}
def set_final():
	fa=open("ips.txt","r")
	for j in fa.readlines():
		fh=open("baba/"+j.strip(),"r")
		c=0
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
		fh.close()

	#for sorting list
	global sram,shd
	sram = sorted(ram.items(),key=operator.itemgetter(1))
	sram.reverse()
	shd = sorted(hd.items(),key=operator.itemgetter(1))
	shd.reverse()

#print (len(shd))
#print(shd)
#print (shd[0][1])

#global task_tracker,data_node
#task_tracker=int(raw_input("how many task_tracker you want to configure: "))

def set_tasktracer(task_tracker) :
	fg=open("task.txt","a")
	task_tracker+=0
	#print (min(task_tracker,len(sram)))
	for i in range(0,min(task_tracker,len(sram))):
		fg.write(sram[i][0])
		fg.write("\n")
	fg.close()


#data_node=int(raw_input("how many data node you want to configure: "))

def set_datanode (data_node):
	fu=open("hd.txt","a")
	for i in range(0,min(data_node,len(shd))):
		fu.write(shd[i][0])
		fu.write("\n")
	fu.close()
