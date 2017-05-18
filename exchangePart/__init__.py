import re

pattern = re.compile(r'云南|杭州|重庆|北京|三亚|哈尔滨|西安')

pn_o = {}
pn_u = {}
with open('input1', encoding='UTF-8') as f:
	for line in f:
		pa = re.search(pattern, line)
		if pa is None:
			continue
		loc = pa.group()
		arr = line.strip('\n').split('\t')
		year = arr[1][0:4]

		for pn in arr[2].split(','):
			pn = pn.strip()
			if pn == 'N/A' or pn == 'N\A':
				continue

			if pn not in pn_o:
				pn_o[pn] = {}
			if year not in pn_o[pn]:
				pn_o[pn][year] = {}

			if loc not in pn_o[pn][year]:
				pn_o[pn][year][loc] = 1
			else:
				pn_o[pn][year][loc] += 1

locationList = ['重庆', '云南', '杭州', '哈尔滨', '西安', '北京', '三亚']
with open('pn_o_output', 'w', encoding='UTF-8') as f:
	for key, value in pn_o.items():
		f.write(key + '\t')
		for location in locationList:
			for year in range(2014, 2017):
				y = str(year)
				if y in pn_o[key]:
					if location in pn_o[key][y]:
						f.write(str(pn_o[key][y][location]) + '\t')
					else:
						f.write('\t')
				else:
					f.write('\t')
		f.write('\n')

# with open('output2016', 'w', encoding='UTF-8') as f:
# 	for key, value in pn_o.items():
# 		f.write(key + '\n')
# 		for k, v in pn_o[key].items():
# 			f.write(k + ' ' + str(v) + ' ')
# 		f.write('\n')
