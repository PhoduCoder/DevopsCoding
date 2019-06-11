import sys

def num_of_min():
	return ( 24*365*60)

if __name__=="__main__":
	
	#input_list=map(int(),sys.argv[1:])  Works only in Python 2
	# In python3 it creates a map class
	# while in python2 it will create a list

	#Below is the python 3 way

	input_list=list(map(int, sys.argv[1:]))
	
	total_min = num_of_min()
	time_to_detect=input_list[0]

	time_to_deploy=input_list[1]

	time_to_restore_db=input_list[2]

	downtime= (time_to_detect+time_to_deploy+time_to_restore_db)
	uptime = (total_min - downtime)
	
	availability = (uptime/total_min)*100

	print ("The availability for this model is {}".format(availability))
