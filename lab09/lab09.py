# lab09 MC102 - 2s2019
# https://www.ic.unicamp.br/~mc102/labs/roteiro-lab09.html


# Função recursiva para busca de palavras
# entradas:	x		posição horizontal no diagrama onde é inicializada a busca
#			y		posição vertical   no diagrama onde é inicializada a busca
#			index_palavra		indice da palavra buscada na lista palavras[]
#			direcao				numero correspondente a direcao de busca (8 dir. posíveis: 0 a 7)
#			index_letra			indice da letra sendo buscada na palavra analisada (deve ser incrementada por 1 a cada iteraçao recursiva)
# saída: 1 se foi encontrada a palavra em algum lugar do diagrama
# 		 0 se não foi encontrada a palavra
def busca_palavra(x, y, index_palavra, direcao, index_letra):
	if index_letra == len(palavras[index_palavra]):
		return(1)	# achou a palavra completa, encerra chamada recursiva
	else:
		# ➡
		if direcao == 0 and (x + index_letra) < len(diagramaIn[y]):	
			if palavras[index_palavra][index_letra] == diagramaIn[y][x + index_letra]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ⬅		
		elif direcao == 1 and (x - index_letra) >= 0:	
			if palavras[index_palavra][index_letra] == diagramaIn[y][x - index_letra]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ⬇ baixo
		elif direcao == 2 and (y + index_letra) < len(diagramaIn):	
			if palavras[index_palavra][index_letra] == diagramaIn[y + index_letra][x]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ⬆	cima
		elif direcao == 3 and (y - index_letra) >= 0:	
			if palavras[index_palavra][index_letra] == diagramaIn[y - index_letra][x]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ↘
		elif direcao == 4 and (y + index_letra) < len(diagramaIn) and (x + index_letra) < len(diagramaIn[y]):	
			if palavras[index_palavra][index_letra] == diagramaIn[y + index_letra][x + index_letra]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ↙
		elif direcao == 5 and (y + index_letra) < len(diagramaIn) and (x - index_letra) >= 0:	
			if palavras[index_palavra][index_letra] == diagramaIn[y + index_letra][x - index_letra]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ↗
		elif direcao == 6 and (y - index_letra) >= 0 and (x + index_letra) < len(diagramaIn[y]):	
			if palavras[index_palavra][index_letra] == diagramaIn[y - index_letra][x + index_letra]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva

		# ↖
		elif direcao == 7 and (y - index_letra) >= 0 and (x - index_letra) >= 0:	
			if palavras[index_palavra][index_letra] == diagramaIn[y - index_letra][x - index_letra]:	# se letra da palavra procurada está na posiçao atual	
				if busca_palavra(x, y, index_palavra, direcao, (index_letra + 1)) == 1:
					adiciona_palavra_out(x, y, index_palavra, direcao)	# adiciona palavra no diagrama de saida
					return(1)											# achou palavra completa, encerra chamada recursiva
				else:
					return(0)
			else:
				return(0)	# letra procurada nao está na posição atual, encerra chamada recursiva		
		else:	# nao encontrou palavra
			return(0)
# fim da definiçao da funçao busca_palavra

# função para substituir palavra encontrada no diagrama de saída
# entradas:	x	posição horizontal da 1a letra da palavra
#			y	posição vertical da 1a letra da palavra
#			index_palavra		índice da palavra na lista palavras[]
#			direcao				numero correspondente a direção da busca (0 a 7)
def adiciona_palavra_out(x, y, index_palavra, direcao):
	# ➡
	if direcao == 0:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y][x + i] = palavras[index_palavra][i]
	# ⬅
	if direcao == 1:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y][x - i] = palavras[index_palavra][i]
	# ⬇ baixo
	if direcao == 2:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y + i][x] = palavras[index_palavra][i]
	# ⬆ cima
	if direcao == 3:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y - i][x] = palavras[index_palavra][i]
	# ↘
	if direcao == 4:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y + i][x + i] = palavras[index_palavra][i]
	# ↙
	if direcao == 5:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y + i][x - i] = palavras[index_palavra][i]
	# ↗
	if direcao == 6:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y - i][x + i] = palavras[index_palavra][i]
	# ↖
	if direcao == 7:
		for i in range(len(palavras[index_palavra])):
			diagramaOut[y - i][x - i] = palavras[index_palavra][i]
# fim da definição da função adiciona_palavra_out


diagramaIn_line = []	# auxiliar para guardar uma linha do diagrama de entrada (funciona como string)
diagramaIn = []			# lista com todas linhas do diagrama de entrada
fim_input = 0			# flag para interromper laço na entrada do diagrama
palavras = []			# lista de palavras a serem analisadas
count = []				# contagem de vezes que cada palavra de palavras[] apareceu
n = 0

# O diagrama de entrada completo, até chegar no numero de palavras a serem analisadas (lê também esse número)
while fim_input == 0:
	diagramaIn_line = []					# "esvazia" string -> nao sei se to usando certo, como eu esvazio uma string sem declarar como lista?
	l = input()								# Lê uma linha da entrada
	if l.isdigit():							# checa se é um digito (no caso, numero de palavras a serem analisadas)
		n = int(l)									# guarda numero de palavras a serem analisadas em n
		fim_input = 1								# altera flag para encerrar laço while
	else:									# se não é um digito
		l = l.split()								# divide entrada a cada "espaço", criando uma lista de caracteres
		for i in range(len(l)):				
			diagramaIn_line += l[i]					# cria uma string com os caracteres lidos da linha, sem espaços
		diagramaIn.append(diagramaIn_line)			# adiciona a linha à lista de linhas

# Lê palavras a serem analizadas, guardando na lista "palavras"
for i in range(n):
	l = input()
	palavras.append(l)
palavras = list(dict.fromkeys(palavras))	# cria um dict (removendo entradas duplicadas), depois transforma dict em lista novamente (list())
n = len(palavras)							# atualiza valor de n, removendo qntd relacionada aos elementos duplicados
palavras.sort()								# coloca elementos da lista em ordem alfabetica

# Cria diagrama base de saída, preenchido por pontos
diagramaOut = [["." for x in range(len(diagramaIn[0]))] for y in range(len(diagramaIn))]


# busca recursiva de palavras usando busca_palavra, guardando contagem em count[]
for i_palavra in range(n):
	count.append(0)
	for y in range(len(diagramaIn)):
		for x in range(len(diagramaIn[y])):
			for direcoes in range(0, 8):
				if busca_palavra(x, y, i_palavra, direcoes, 0) == 1:
					count[i_palavra] += 1

# imprime diagrama de saida
for i in range(len(diagramaIn)):
	for j in range(len(diagramaIn[0])):
		print(diagramaOut[i][j], end="")
		if j < (len(diagramaIn[0]) - 1):
			print(" ", end="")
	if i < len(diagramaIn):
		print()

# Imprime palavras e respectivas contagens
for i in range(n):
	print(palavras[i], end=': ')
	print(count[i])
