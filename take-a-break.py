#!/usr/bin/python



#      requirements:
#
#           xprintidle ( apt-get install xprintidle )
#           python-notify  ( apt-get install python-notify )
#
import sys
import pynotify
import subprocess
import time

if __name__ == "__main__":
	if not pynotify.init("icon-summary-body"):
	    sys.exit(1)

	# init default variables
	timeout_sec 			= 60.0 # in SECONDS	
	idle_treshold			= 15.0 # in minutes
	notify_minutes	 		= 60.0 # in minutes


	# main loop
	mins_passed = 0.1
	while (True):
		# sleep, count minutes slept
		time.sleep(timeout_sec)		
		mins_passed = mins_passed + ( timeout_sec / 60.0 ) # convert from sec to minutes
		print '\nminutes passed: ' + str(mins_passed)

		# if idle last 'idle_treshold' minutes then reset timer
		p = subprocess.Popen(['xprintidle'], stdout=subprocess.PIPE) # get idle time from system
		p.wait()
		idle_mins = float(p.stdout.read()) / 1000 / 60 # convert from miliseconds to minutes
		print 'minutes idle: ' + str(round(idle_mins, 3))
		if idle_mins > idle_treshold:
			mins_passed = 0.1

		# show notification every hour ( or so )
		if mins_passed > notify_minutes:
			n = pynotify.Notification(
						    "Take A Break",
						    "Remmember to take a 5 min break every hour",
						    "dialog-information") # notification-message-im
			n.show()
			mins_passed = 0.1 # reset minutes counter


	
