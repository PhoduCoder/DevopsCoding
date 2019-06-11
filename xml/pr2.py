from xml.etree import ElementTree

with open('data.xml', 'r+') as f:
	tree=ElementTree.parse(f)

for node in tree.iter():
	if (node.tag=='with_attributes'):
		print (node.tag)
		print (node.attrib, type(node.attrib))
