#!/usr/bin/python
import sys
import pynotify
import subprocess
import time

if __name__ == "__main__":
	if not pynotify.init("icon-summary-body"):
	    sys.exit(1)

	# init default variables
	default_timeout_sec 		= 60.0 # !SECONDS	
	default_idle_treshold		= 15.0 # minutes
	notification_treshold_minutes 	= 60.0 # minutes
	mins_passed 			= 0.1

	# main loop
	while (True):
		# sleep, count minutes slept
		time.sleep(default_timeout_sec)
		#mins_passed = mins_passed + ( float(default_timeout_sec) / 60.0 )
		mins_passed = mins_passed + ( default_timeout_sec / 60.0 )
		print '\nminutes passed: ' + str(mins_passed)

		# if idle last N minutes then reset timer
		p = subprocess.Popen(['xprintidle'], stdout=subprocess.PIPE)
		p.wait()
		idle_mins = float(p.stdout.read()) / 1000 / 60  # minutes
		print 'minutes idle: ' + str(round(idle_mins, 3))

		if idle_mins > default_idle_treshold:
			mins_passed = 0.1

		# show notification every hour ( or so )
		if mins_passed > notification_treshold_minutes:
			n = pynotify.Notification(
			    "Take A Break",
			    "Remmember to take a 5 min break every hour",
			    "dialog-information") # notification-message-im
			n.show()
			mins_passed = 0.1

#	p = subprocess.Popen(['xprintidle'], stdout=subprocess.PIPE)
#	p.wait()

#	idle_mins = float(p.stdout.read()) / 1000 / 60  # hours




	
