#!/usr/bin/python2
import os
import sys
os.system("yum install hadoop -y")
os.system("yum install jdk -y")
os.system("rm -rf /data")
os.system("mkdir /data")

#hdfs
fh=open("/etc/hadoop/hdfs-site.xml","w")
x='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<!--testing 1--> 
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/data</value>
</property>

</configuration>'''
# writing files
fh.write(x)
fh.close()

fo=open("/root/Desktop/task.txt","r")
i=fo.readline()
i=i.strip()
print(i)
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

os.system("hadoop-daemon.sh  stop datanode")
os.system("hadoop-daemon.sh  start datanode")

