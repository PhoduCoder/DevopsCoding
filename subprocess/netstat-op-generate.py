import sys
import subprocess

cmd_list=sys.argv[1:]

print (cmd_list)

print ("==========")

#cmd= ["netstat", "-anp" ,"|", "grep" ,":80"]

result=subprocess.run(cmd_list, shell=True)

print (result)
