# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que permite criar uma matriz.
#

from model.matriz_de_inteiros import MatrizDeInteiros

class PainelCriaMatriz:

    def crie(self, iu, nome):
        print('- - - Criar Matriz {} - - - '.format(nome))
        nl = int(input('Quantas linhas:  '))
        nc = int(input('Quantas colunas: '))
        matriz = MatrizDeInteiros((nl, nc))
        iu.armazene_matriz(nome, matriz)
        print('Matriz criada!')
        input('Tecle ENTER para continuar')
