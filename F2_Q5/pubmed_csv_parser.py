file = open('europepmc.csv', 'r', encoding="utf8")
file_content = file.read().split('\n', 1)

publications = file_content[1].split('\n')

results = []

for paper in publications:
	print(paper)
	info = paper.split(',')
	pmid = info[0].replace('"', '')
	pmcid = info[1]
	date = info[2]
	date = date.split('-')
	try:
		formated_date = f"{date[2]}/{date[1]}/{date[0]}"
	except:
		date = ['1', '1', '3000']
	if int(date[2])<2023:
		results.append(f"{pmid},{pmcid},{formated_date}")
	elif int(date[2])==2023:
		if int(date[1])<4:
			results.append(f"{pmid},{pmcid},{formated_date}")

with open('results2.txt', 'w') as file:
	file.write('\n'.join(results))