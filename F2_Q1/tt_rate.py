from Bio import SeqIO
seq_dict = {rec.id : rec.seq for rec in SeqIO.parse("caso_de_teste_0.fasta", "fasta")}

def find_inequalities(seq1, seq2):
	inequalities = []
	for i in range(0, len(seq1)):
		if seq1[i] != seq2[i]:
			inequalities.append([seq1[i], seq2[i]])
	return inequalities

def classify_inequalities(ineq_list):
	transitions = 0
	transversions = 0
	for ineq in ineq_list:
		if 'A' in ineq:
			if 'G' in ineq:
				transitions += 1
			else:
				transversions += 1
		elif 'C' in ineq:
			if 'T' in ineq:
				transitions += 1
			else:
				transversions += 1
		else:
			transversions += 1
	return transitions, transversions

ineq_list = find_inequalities(seq_dict['seq1'], seq_dict['seq2'])
transitions, transversions = classify_inequalities(ineq_list)
ratio = "{:.3f}".format(transitions/transversions)
print(ratio)