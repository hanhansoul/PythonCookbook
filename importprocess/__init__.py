import re

inputFileName = "D:\import1"
outputFileName = 'D:\import320'
result = ''

with open(inputFileName, 'r') as f:
	content = f.read()
	result = re.sub(' +', ' ', content)
	# result = re.sub('^', '(\'', result)
	# result = re.sub('$', '\')', result)
	# result = re.sub(' ', '\', \'', result)
	print(result)

with open(outputFileName, 'w') as f:
	f.write(result)

