chars =words =lines = 0
with open('test.txt','r') as in_file:
	for line in in_file:
		lines += 1
		words +=len(line.split())
		chars +=len(line)
print(lines)
print(words)
print(chars)