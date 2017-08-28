import os
import time
import sys

try:
	while True:
		x = os.system('ping google.com -c 4 -t 3')
		
		if x == 0:
			print("up")
			os.system("say internet is up") #macOnly
		else:
			print("down")
			os.system("say internet is down") #macOnly
		
		time.sleep(int(sys.argv[1]) if len(sys.argv) > 1 else 57)

except KeyboardInterrupt:
	print()
	exit(0)