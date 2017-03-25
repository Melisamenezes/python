from xml.dom.minidom import parse
dom = parse("test.xml")
for node in dom.getElementsByTagName('plant'):
	id = node.getAttribute('id')
	print("Plant ID :",id)
	common = node.getElementsByTagName('common')[0].childNodes[0].nodeValue
	print("Common: ",common)
	botanical = node.getElementsByTagName('botanical')[0].childNodes[0].nodeValue
	print("Botanical: ",botanical)
	zone = node.getElementsByTagName('zone')[0].childNodes[0].nodeValue
	print("Zone: ",zone)
