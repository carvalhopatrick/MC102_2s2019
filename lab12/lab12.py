# lab12 - MC102 2s2019
# https://www.ic.unicamp.br/~mc102/labs/roteiro-lab12.html

# Função print_moldura()
# Printa triangulo armazenado em "tela" com uma moldura aidicional, conforme pedido no enunciado do laboratório
def print_moldura():
	telaMoldura = [ [" " for j in range(largura + 4)] for i in range(altura + 4)]

	auxStr = ["-" for i in range(largura + 2)]

	telaMoldura[0] = "+" + "".join(auxStr) + "+"
	telaMoldura[altura + 3] = "+" + "".join(auxStr) + "+"
	
	auxStr = [" " for i in range (largura + 2)]
	telaMoldura[1] = "|" + "".join(auxStr) + "|"
	telaMoldura[altura + 2] = "|" + "".join(auxStr) + "|"

	for i in range(altura):
		telaMoldura[i+2] = "| " + "".join(tela[i]) + " |"

	for i in range(len(telaMoldura)):
		print(telaMoldura[i])

# Função triangulo_branco()
# Desenha triangulo branco em "tela" a partir de coordenadas x (coluna) e y (linha)
# x
def triangulo_branco(x, y):
	x += 1
	for i in range(altura_branco):
		for j in range(largura_branco - (2 * i)):
			tela[y + i][x + j] = " "


#########################################################################################

# Lê parâmetros de entrada
altura = int(input())
largura = (2 * altura) - 1
profundidade = int(input())
char_preto = "*" ###############################

# Cria matriz inicial "tela" vazia, onde será criado o triângulo
tela = [ [" " for j in range(largura)] for i in range(altura)]

# Cria triângulo inicial em "tela"
for i in range(altura):
	pos = (largura // 2)
	for j in range(i+1):
		tela[i][pos + j] = char_preto
		tela[i][pos - j] = char_preto
	

print_moldura()

for p in range(profundidade):
	altura_branco = 2**(altura - (p + 1))
	largura_branco = (2 * altura_branco) - 1
	for i in range(altura):
		for j in range(largura):
			count = 0
			espaco_branco = False
			print()
			while (espaco_branco == False) and (count < (largura)):
				if tela[i][j + count] == char_preto:
					count += 1
				else:
					espaco_branco = True
				print(count)
				
			if count == (largura_branco + 2):
				triangulo_branco(i, j)

print()
print_moldura()
