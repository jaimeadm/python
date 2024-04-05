# Importing required module
import subprocess
import os

# Using system() method to
# execute shell commands
subprocess.Popen('ls', shell=True)
os.system('echo "ola"')
