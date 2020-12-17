# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que permite inserir números em uma matriz.
#

from view.util import mostra_matriz

class PainelPovoaMatriz:

    def povoe(self, nome, matriz):
        print('- - - Povoando Matriz {} - - - '.format(nome))
        mostra_matriz(matriz, 5)
        alterar = 's' == input('Alterar ? [s/n] ')
        nl = matriz.num_linhas()
        nc = matriz.num_colunas()
        while alterar:
            l = int(input('Linha (1 a {}): '.format(nl)))
            c = int(input('Coluna (1 a {}): '.format(nc)))
            numero = int(input('Número: '))
            matriz.armazene(l,c,numero)
            mostra_matriz(matriz, 5)
            alterar = 's' == input('Alterar ? [s/n] ')
        input('Tecle ENTER para continuar')
