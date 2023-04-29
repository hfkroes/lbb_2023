def respiracao_ou_fermentacao(experimentos):
	escolha_de_reacao = []
	for experimento in experimentos:
		Y = int(experimento[0])
		Z = int(experimento[1])
		if (38 / (Y + (6 * Z))) >= 2/Y:
			escolha_de_reacao.append("R")
		else:
			escolha_de_reacao.append("F")
	return escolha_de_reacao

def quanto_atp(reacao, experimentos):
	producao_de_atp = []
	for i in range(len(experimentos)):
		Y = int(experimentos[i][0])
		Z = int(experimentos[i][1])
		X = int(experimentos[i][2])
		if reacao[i] == 'R':
			ATP = 38 * (X / (Y + (6 * Z)))
			producao_de_atp.append("{:.3f}".format(ATP))
		elif reacao[i] == 'F':
			ATP = 2 * (X / Y)
			producao_de_atp.append("{:.3f}".format(ATP))
	return producao_de_atp

file = open('caso_de_teste_2.txt', 'r')
file_content = file.read().split('\n', 1)

m = int(file_content[0])
experimentos = [i.split('\t') for i in file_content[1].split('\n')]

reacoes = respiracao_ou_fermentacao(experimentos)
resultados = quanto_atp(reacoes, experimentos)

print('\n'.join(resultados))