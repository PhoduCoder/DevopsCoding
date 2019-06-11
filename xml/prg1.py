from xml.etree import ElementTree


with open('sample.xml', 'r+') as f:
	tree = ElementTree.parse(f)

total_score=0
for node in tree.iter():
	list_of_attrib=list(node.attrib)
	#print (list_of_attrib)
	score=len(list_of_attrib)
	total_score+=score
	#print (score)	

print (total_score)
