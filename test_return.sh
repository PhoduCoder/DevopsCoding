function foo {
	#return 5
	echo "Hello world"
	}

foo

echo $?

#Command Substitution

#echo $(command)
echo $(pwd)


echo `command`
echo `top`

#arithmetic substitution

$((3+5))


#execute a command in the sub shell
#(command list)

(cd ; ls -la;)

#execute a command in the same shell
#{command list}

{cd ; ls -la;}

#both of these has the last run command status returned as the exit status

