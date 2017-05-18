import re

pattern = re.compile(r'云南|杭州|重庆|北京|三亚|哈尔滨|西安')
pno = {}
pnu = {}
locationList = ['重庆', '云南', '杭州', '哈尔滨', '西安', '北京', '三亚']

def init_dict():
	protype = {}
	for loc in locationList:
		protype[location] = {}
		for y in range(2014, 2017):
			protype[loc][y] = 0
	return protype

def count(input, counter, location, year):
	for pn in input.split(','):
		pn = pn.strip()
		if pn == 'N/A' or pn == 'N\A':
			continue
		if pn not in counter:
			counter[pn] = init_dict()
		counter[pn][location][year] += 1

def output(output_file_name, counter):
	with open(output_file_name, 'w', encoding='UTF-8') as f:
		for pn, d in counter.items():
			f.write(pn + '\t')
			for loc in locationList:
				for y in range(2014, 2017):
					if d[loc][y] > 0:
						f.write(str(d[loc][y]) + '\t')
					else:
						f.write('\t')
			f.write('\n')

with open('input1', encoding='UTF-8') as f:
	for line in f:
		pa = re.search(pattern, line)
		if pa is None:
			continue
		location = pa.group()
		arr = line.strip('\n').split('\t')
		year = int(arr[1][0:4])
		count(arr[2], pno, location, year)
		count(arr[3], pnu, location, year)

output('pn_o_output', pno)
output('pn_u_output', pnu)
