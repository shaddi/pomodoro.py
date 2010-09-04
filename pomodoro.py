#!/usr/bin/python
#
# pomodoro.py: a little script to help your productivity.
# Shaddi Hasan, 2010. http://sha.ddih.org.
#
# pomodoro.py is a simple script to help increase your focus and productivity.
# After you run the script, you'll have ten minutes of uninterrupted work time,
# which is enforced by disabling your network adapters. When ten minutes is up,
# you've earned a two minute break, and your network adapters will be brought
# back up. 
#
# To run this, make sure you have the required imports on your system, then 
# modify the interfaces lists below to reflect the names of your system's 
# network adapters. Then run:
#
#          $ sudo pomodoro &
# 
# If you need to kill it, open up another terminal and kill the process (but 
# resist the temptation!). 

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
sec_to_run = 3*60*60 # 3 hour total runtime
work_time = 10*60 # 10 minutes of work time
rest_time = 2*60 # 2 minutes of break time

# Other settings
disable_network = True # Set to false if the internet isn't a distraction to you (?!)
disable_interrupts = True # Makes it a little harder to kill (but not much)

# modify the interfaces list to match your particular system...
def turn_off_internet():
	interfaces = ["eth0","wlan0"]
	for interface in interfaces:
		os.system("ifconfig " + interface + " down")

def turn_on_internet():
	interfaces = ["eth0","wlan0"]
	for interface in interfaces:
		os.system("ifconfig " + interface + " up")

end_time = int(time.time()) + sec_to_run

# Main loop
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
	


