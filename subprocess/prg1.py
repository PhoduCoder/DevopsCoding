import subprocess
import sys

print (sys.argv)

cmd_list = sys.argv[1:]

#cmd=["ls", "-lrth"]

completed = subprocess.run(cmd_list)

print ("Completed Code:" ,completed.returncode)

if (completed.returncode == 0):
	print ("Command was successful")

else:
	print ("Command was not successful")
