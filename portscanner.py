#!/bin/python3

print("\n" * 3)
print(""" _____ _                 _       ______          _     _____                                 
/  ___(_)               | |      | ___ \        | |   /  ___|                                
\ `--. _ _ __ ___  _ __ | | ___  | |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
 `--. \ | '_ ` _ \| '_ \| |/ _ \ |  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
/\__/ / | | | | | | |_) | |  __/ | | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\____/|_|_| |_| |_| .__/|_|\___| \_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   
                  | |                                                                        
                  |_|""")
print("An Adaptation of the Port Scanner from TCM Security PEH Course by @daycyberwox")

import sys  #systems functions and parameters
import socket   #defines how server and client machines can communicate
from datetime import datetime   #date and time module


# Starting time of the program
start = datetime.now()

def nl(): #defining the function for a new line
	print('\n')

# Define our target
if len(sys.argv) == 2:  #if there are 2 arguments present
        target =  socket.gethostbyname(sys.argv[1]) #Translating a hostname to IPv4
else:
        print("Invalid amount of arguments")
        print("Syntax: python3 portscanner.py <ip>")


# Add a pretty banner
print("-" * 50) #print 50 dashes
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)


try:
        for port in range(50,85):   #for every port between 50 & 85
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #AF_INET is basically IPv4 and #SOCK_STREAM is basically the port
                socket.setdefaulttimeout(1) #attempts to connect to a port and if the port is not connectible, waits 1 second and moves to the next port
                result = s.connect_ex((target,port))    #returns an error indicator and stores it in the "result" variable
                #print("Checking port {}".format(port))
                if result == 0:
                        print("Port {} is open".format(port))
                s.close()   #closes the connection

except KeyboardInterrupt:   #if there's a keyboard interruption like ctrl + c
        print("\nExiting Program.")
        sys.exit()  #facilitates a clean exit

except socket.gaierror: #gai stands for getaddressinfo - basically DNS issue
        print("\nHostname could not be resolved!")
        sys.exit()

except socket.error:    #if a connection cannot be made to the address
        print("Couldn't connect to server :( ")
        sys.exit()

# Ending time of the program
end = datetime.now()

nl()
print("Scanning Completed!")

# Show time difference between starting and ending time
print("-" * 50)
print("This script completed in "+str(end-start)[5:]+" seconds")