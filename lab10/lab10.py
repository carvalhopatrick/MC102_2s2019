# lab10 - MC102 2s2019
# https://www.ic.unicamp.br/~mc102/labs/roteiro-lab10.html

paginas = []
fim_input = False
links = []
linksInv = []
listAux =  []
listAux2 = []
d = 0.875		# fator de amortecimento

# Guarda entrada de paginas em lista
l = input()
paginas = l.split()
nPaginas = len(paginas)			# numero de paginas

# Guarda links das paginas
while fim_input == False:
	l = input()
	if not (l.isdigit()):	# se entrada nao for um digito (é um link)
		links.append(l)			# adiciona string na lista de links
		l = l[::-1]				# inverte string l (ex:  A -> B   |||   B >- A ), facilitará solução
		linksInv.append(l) 		# adiciona string invertida na lista de links inversos
	else:						# entrada é um digito (numero de passos a serem calculados)
		nPassos = int(l)	
		fim_input = True		# atualiza flag para encerrar laço de leitura		

links = list(dict.fromkeys(links))	# remove entradas duplicadas na lista
links.sort()						# organiza elementos em ordem alfabetica
linksInv = list(dict.fromkeys(linksInv))	# faz o mesmo para a lista com strings invertidas
linksInv.sort()
refsOrigem = dict.fromkeys(paginas)			# dicionario de origem de referencias  (paginas que referenciaram a pagina-chave)
refsDestino = dict.fromkeys(paginas)		# dicionario de destino de referencias (paginas referenciadas pela pagina-chave)


# Cria dicionario ORIGEM, onde cada chave é uma pagina.
	# Dentro de cada chave, haverá uma lista de paginas que referenciou a pagina indicada por essa chave
# Também cria dicionário DESTINO, onde cada chave é uma página
	# Dentro de cada chave, haverá uma lista de paginas que foram referenciadas pela página indicada por essa chave.
for i in range(nPaginas):
	for j in range(len(links)):
		# Destino
		# primeiro caracter de links se refere a pagina que está referenciando outra. Se for a pagina em questao, vamos adicionar a lista de refs dessa pagina
		if links[j][0] == paginas[i]:
			if links[j][len(links[j]) - 1] != paginas[i]:			# não considera paginas que referenciam a si mesmo
				listAux.append(links[j][len(links[j]) - 1])			# adiciona pagina referenciada por pagina[i], que esta no ultimo caracter de links[j]
		# Origem
		# primeiro caracter de linksInv se refere a pagina referenciada. Se for a pagina em questao, vamos adicionar a lista de refs dessa pagina
		if linksInv[j][0] == paginas[i]:
			if linksInv[j][len(linksInv[j]) - 1] != paginas[i]:			# não considera paginas que referenciam a si mesmo
				listAux2.append(linksInv[j][len(linksInv[j]) - 1])		# adiciona pagina que referenciou a pagina[i], que está no ultimo caracter de linksInv[j]
	
	refsDestino[paginas[i]] = listAux	# coloca lista de paginas que referenciadas por pagina[i] na chave da pagina[i] do dicionario
	listAux =  []						# esvazia lista	auxiliar para ser reutilizada
	refsOrigem[paginas[i]] = listAux2	# coloca lista de paginas que referenciou pagina[i] na chave da pagina[i] do dicionario
	listAux2 = []						# esvazia lista	auxiliar para ser reutilizada


# Cria lista pageRank, onde cada elemento corresponde a um passo
# Em cada passo, haverá um dicionário com todas as páginas analisadas  -->  pageRank[0]["A"] = PageRank 0 da página A.
pageRank = []
for i in range(nPassos+1):
	pageRank.append(dict.fromkeys(paginas))

# Calcula pageRank[passo][pagina]
for i in range(nPassos+1):
	for j in paginas:
		if i == 0:
			# Calcula PR0
			pageRank[i][j] = 1/nPaginas
		else:
			# Calcula PRi
			soma = 0
			for k in paginas:
				if k != j and k in refsOrigem[j]:	# se há referencia para pagina[j] em pagina[k]
					soma += pageRank[i-1][k] / len(refsDestino[k])
			pageRank[i][j] = (1 -d)/nPaginas + (d * soma)


# Imprime saída
for i in paginas:
	print("{} -> {}".format(i, refsDestino[i]))
	print("{} -> {}".format(refsOrigem[i], i))

for i in range(nPassos+1):
	print("PageRank (passo {})".format(i))
	for j in paginas:
		print("{}: {:.3f}".format(j, pageRank[i][j]))
