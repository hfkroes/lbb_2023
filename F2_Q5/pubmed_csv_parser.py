file = open('sys_alzheimer2.csv', 'r', encoding="utf8")
file_content = file.read().split('\n', 1)

publications = file_content[1].split('\n')

results = []

for paper in publications:
	info = paper.split('","')
	pmid = info[0].replace('"', '')
	pmcid = info[8]
	date = info[7]
	date = date.split('/')
	date = f"{date[2]}/{date[1]}/{date[0]}"

	results.append(f"{pmid},{pmcid},{date}")

with open('results.txt', 'w') as file:
	file.write('\n'.join(results))