#!/home/dcj/miniconda3/bin/python

import sys
import os
import subprocess
#from time import sleep
import shlex
import cgi
sys.stdout.write("Content-Type: text/plain\n\n")
#print("Content-Type: text/plain; charset=utf-8\n")
#print('')
sys.stdout.flush()

os.chdir("/var/www/html/")
subprocess.run('rm -rf usr', shell=True)
subprocess.run('mkdir usr',shell=True)
subprocess.run('cp -r usr-backup/* usr/', shell=True)
subprocess.run('chmod -R 777 usr', shell=True)
