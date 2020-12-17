# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que permite multiplicar duas matrizes.
#

from view.util import mostra_matriz

class PainelMultiplicaMatrizes:

    def multiplique(self, nomeA, matrizA, nomeB, matrizB):
        print('- - - Multiplicar Matrizes {} e {}'.format(nomeA, nomeB))
        print('Matriz {}:'.format(nomeA))
        mostra_matriz(matrizA, 5)
        print('Matriz {}:'.format(nomeB))
        mostra_matriz(matrizB, 5)  
        print('Multiplicando...')     
        multiplicada = matrizA * matrizB
        if multiplicada is None:
            print('Não é possível multiplicar.')
        else:
            print('Matriz Resultante:')
            mostra_matriz(multiplicada, 5)
        input('Tecle ENTER para continuar') 