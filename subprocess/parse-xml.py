from xml.etree import ElementTree

with open('sample.xml', 'r+') as f:
	tree = ElementTree.parse(f)

for node in tree.iter():
	if (node.tag == "outline"):
		print (node.attrib.get('text'), node.attrib.get('htmlUrl'))

	#print (node.tag, node.attrib)

print (dir(node))
