# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que permite somar duas matrizes.
#

from view.util import mostra_matriz

class PainelSomaMatrizes:

    def some(self, nomeA, matrizA, nomeB, matrizB):
        print('- - - Somar Matrizes {} e {}'.format(nomeA, nomeB))
        print('Matriz {}:'.format(nomeA))
        mostra_matriz(matrizA, 5)
        print('Matriz {}:'.format(nomeB))
        mostra_matriz(matrizB, 5)  
        print('Somando...')     
        soma = matrizA + matrizB
        if soma is None:
            print('Não é possível somar.')
        else:
            print('Matriz Resultante:')
            mostra_matriz(soma, 5)
        input('Tecle ENTER para continuar') 