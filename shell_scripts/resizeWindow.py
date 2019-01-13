import sys
from subprocess import call
import subprocess
import os
import envoy
import sh


#Add the below commented lines to your .bashrc and uncomment it.
#  function prompt {  

#  #!/bin/bash
# if [ -e ~/temporary.txt ]
# then    
#     history > ~/temporary.txt
# else    
#     touch ~/temporary.txt
#     history > ~/temporary.tt
# fi

#  
#   #Here paste the path where you copied the resizeWindow.py file.
#   python ~/resizeWindow.py

# }

# PROMPT_COMMAND=prompt




with open("/home/sourabh/temporary.txt", "rb") as f:
    first = f.readline()        
    f.seek(-2, os.SEEK_END)     
    while f.read(1) != b"\n":   
        f.seek(-2, os.SEEK_CUR) 
    last = f.readline() 
   
last = last.split(' ')[4:]
line = ' '.join(last)

line = line[:-1]




horizontalSuspects = ['docker container ls','htop','ls','git log']

verticalSuspects = ['ll','history']


if line is "":
	call(['printf',"'\033[8;24;80t'"])

if any( command in line for command in horizontalSuspects):	
	call(['printf',"'\033[8;34;154t'"])
	exit()

elif any( command in line for command in verticalSuspects):
	call(['printf',"'\033[8;52;85t'"])	
	exit()
	
else:
	call(['printf',"'\033[8;24;80t'"])
