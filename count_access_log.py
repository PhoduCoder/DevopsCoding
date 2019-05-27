import re

def log_parser(log):
	matches_list=[]
	with open(log,'r') as f:
		log_line=f.read()
		#print (log_line)
		regexp_for_ip=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
		python_re_object=re.compile(regexp_for_ip)
		matches_list=python_re_object.findall(log_line)

		from collections import Counter
		matches_count_dict=Counter(matches_list)
		
	print (matches_count_dict)

	for key, values in matches_count_dict.items():
		print ("{} has {} occurences" .format(key, values))
		

if (__name__=="__main__"):
	log_parser("access_log.txt")
