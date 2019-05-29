import re

def recvq_sum(file):
	with open(file, 'r') as f:
		test_string=f.read()
		#test_list=f.readline()
	#print (type(test_list), test_list)
	print (type(test_string), test_string)

def count_lines(file):
	with open(file, 'r') as f:
		file_contents=f.read()
		pattern=re.compile(r"\n")
		matches_count=pattern.findall(file_contents)
		num_of_lines=len(matches_count)

		print (num_of_lines)


if (__name__=="__main__"):
	#recvq_sum("netstat-op.txt")

	count_lines("netstat-op.txt")
