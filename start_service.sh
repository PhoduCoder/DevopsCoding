import subprocess

#This script is used to check 
#for the status of a command.

#If the script encounters that the command
#is not running, the script will try 
#to start the command

cmd_check=["ps","-C", "sshd"]

#service_status=subprocess.call(["ps", "-C", "sshd"])
service_status=subprocess.call(cmd_check)

if (service_status==0):
	print ("Service running properly")
else:
	print ("service not running\n")
	print ("Attempting to restart the service\n")

	subprocess.call(["systemctl", "start", "sshd"])

	#service_status=subprocess.call(["ps", "-C", "sshd"])
	service_status=subprocess.call(cmd_check)

