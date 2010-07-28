#!/usr/bin/python

import pynotify
import os
import time

# Notifications
pynotify.init("pomodoro.py")
work = pynotify.Notification("Here we go!","Time to get to work!")
work.set_timeout(3)
rest = pynotify.Notification("Break!","Good job! You earned a break!")
rest.set_timeout(3)

# Timings
sec_to_run = 3*60*60
work_time = 10*60
rest_time = 2*60

# Other settings
disable_network = True
disable_interrupts = True

def turn_off_internet():
	os.system("ifconfig eth0 down")
	os.system("ifconfig wlan0 down")

def turn_on_internet():
	os.system("ifconfig eth0 up")

end_time = int(time.time()) + sec_to_run

while int(time.time()) < end_time:
	try:
		# work for a bit
		work_start = int(time.time())
		work.show()
		while int(time.time()) < (work_start + work_time):
			if disable_network:
				# disable the network adapters!
				turn_off_internet()

			time.sleep(10)

		# now rest
		rest.show()
		if disable_network:
			# re-enable the network adapters
			turn_on_internet()

		time.sleep(rest_time)

	except:
		if disable_interrupts:
			continue
		else:
			break

final_note = pynotify.Notification("That's the end of it!","Great job being productive!")
final_note.set_timeout(5)
final_note.show()
	


