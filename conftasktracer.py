#!/usr/bin/python2
import os
import sys
os.system("yum install hadoop -y")
os.system("yum install jdk -y")

fh=open("/etc/hadoop/mapred-site.xml","w")

fo=open("/root/Desktop/task.txt","r")

i=fo.readline()
i=fo.readline()
i=i.strip()

fo.close()

#mapred
x='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>mapred.job.tracker</name>
<value>'''+i+''':9002</value>
</property>
</configuration>'''

fh.write(x)
fh.close()

os.system("hadoop-daemon.sh stop tasktracker")
os.system("hadoop-daemon.sh start tasktracker")


