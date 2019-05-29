import subprocess

#We will try and understand the difference
#between shell=True and not using
#it in the subprocess module


#When not using the shell=True

subprocess.run(["echo", "$HOME"])


#When using shell=True
#The shell before running the command
#will preprocess all the variables,
#globs and other shell features in the command
#before processing it

subprocess.run(["echo $HOME"], shell=True)

#also notice that when Shell=True is set
#all the commands can be passed without making them
#as separate elements of the list

#This appears as if the command is directly executed on the shell
