def discover_incompatibility_sequence(seq_list):
	igs_list = []
	for test in seq_list:
		seq1 = test[0]
		seq2 = test[1]
		min_igs = ""
		for i in range(len(seq1)):
			for j in range(i+1, len(seq1)+1):
				seq = seq1[i:j]
				if seq in seq2:
					continue
				if len(min_igs) == 0 or len(seq) < len(min_igs):
					min_igs = seq
		igs_list.append(min_igs)
	return igs_list

def calculate_incompatibility_degree(m, seq_list, inc_seq):
	inc_deg_list = []
	for i in range(m):
		G = len(seq_list[i][0])
		k = len(inc_seq[i])
		B = G / (1 + (k**2))
		inc_deg_list.append("{:.3f}".format(B))
	return inc_deg_list

file = open('caso_de_teste_4.txt', 'r')
file_content = file.read().split('\n', 1)

m = int(file_content[0])
tests = file_content[1][:-3].split('\n--\n')
seq_list = []
for sequences in tests:
	i, j = sequences.split('\n')
	seq_list.append([i, j])

inc_seq = discover_incompatibility_sequence(seq_list)
test_results = calculate_incompatibility_degree(m, seq_list, inc_seq)

print('\n'.join(test_results))

