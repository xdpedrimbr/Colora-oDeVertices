###################################################################
# Grupo:                                                          #
# Pedro Henrique Gonçalves Teixeira - 11821BCC008                 #
# Marillia Soares Rodrigues - 11821BCC020                         #
# Hendrik Abdalla Hermann - 11911BCC034                           #
#                                                                 #
###################################################################

import time

class gerarGrafo():
    def __init__(self, numVertices):
        self.vertices = numVertices
        self.grafo = [[0 for colunas in range(numVertices)]\
                            for linhas in range(numVertices)]

    def checkProx(self, vertice, cor, corAtual):
        for c in range(self.vertices):
            if self.grafo[vertice][c] == 1 and cor[c] == corAtual:
                return False
                
        return True

    def defineCor(self, qtdCor, cor, vertice):
        if vertice == self.vertices:

            return True

        c = 1
        while c <  qtdCor + 1:
            if self.checkProx(vertice, cor, c) == True:
                cor[vertice] = c
                if self.defineCor(qtdCor, cor, vertice + 1) == True:
                    return True
                cor[vertice] = 0
            c = c + 1

    def colorir(self, qtdCor):
        cor = [0] * self.vertices
        if self.defineCor(qtdCor, cor, 0) == None:
            return False

        for c in cor:
            print(c)

        return True

####### MAIN #######
n = int(input("Digite a quantidade de vertices do grafo (5, 6, 7, 8, 9): "))
grafo = gerarGrafo(n)

q = int(input("Digite a quantidade de cores: "))
qtdCor = q

print(f"O grafo tera {n} vertices!\n")

vetor = []
matriz = []
temp = 0

print("Agora, digite elemento por elemento do grafo (0 ou 1) ou abra os arquivos .txt de exemplos de matrizes e cole os exemplos no terminal: \n")
for c in range (n):
    vetor = []
    for i in range (n):
        print(f'Digite o elemento {c + 1}x{i + 1}: ', end='')
        temp = int(input())
        vetor.append(temp)
    matriz.append(vetor)

#print(f"\nA matriz eh: ")
print(matriz)

print(f"As cores (1 a {q}) foram: ")
tempo1 = time.time()
grafo.grafo = matriz
grafo.colorir(qtdCor)
tempo2 = time.time()

tempoDeExecucao = tempo2 - tempo1
print(f"\nO tempo de execucao para {n} vertices foi: {tempoDeExecucao}\n")

# vetorTempo = []
# for i in range(1, 31):
#     tempo1 = time.time()
#     grafo = gerarGrafo(9)
#     qtdCor = 4
#     grafo.grafo = [[0, 1, 1, 1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 0], [1, 
# 1, 0, 1, 0, 1, 0, 1, 0]]
#     grafo.colorir(qtdCor)
#     tempo2 = time.time()

#     tempoDeExecucao = tempo2 - tempo1
#     print(f"\nO tempo de execucao para 5 vertices foi: {tempoDeExecucao}\n")
#     vetorTempo.append(tempoDeExecucao)

# print(vetorTempo)