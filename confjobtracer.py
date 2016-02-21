#!/usr/bin/python2
import os
import sys
os.system("yum install hadoop -y")
os.system("yum install jdk -y")

fo=open("/root/Desktop/task.txt","r")
i=fo.readline()
j=fo.readline()
print i
print j
i=i.strip()
j=j.strip()
fo.close()

#core

fh=open("/etc/hadoop/core-site.xml","w")
x='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--testing 1--> 
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://'''+i+''':9001</value>
</property>
</configuration>'''

fh.write(x)
fh.close()
fh=open("/etc/hadoop/mapred-site.xml","w")
#mapred
x='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>mapred.job.tracker</name>
<value>'''+j+''':9002</value>
</property>
</configuration>'''

fh.write(x)
fh.close()

os.system("hadoop-daemon.sh stop jobtracker")
os.system("hadoop-daemon.sh start jobtracker")
