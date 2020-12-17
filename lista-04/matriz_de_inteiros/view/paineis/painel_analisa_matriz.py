# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que permite exibir informações sobre uma matriz.
#

from view.util import mostra_matriz

class PainelAnalisaMatriz:

    def analise(self, matrizes):
        print('- - - Analisando Matriz - - -')
        matriz = self._escolha_matriz(matrizes)
        while matriz is not None:
            self._mostre_matriz(matriz)
            matriz = self._escolha_matriz(matrizes)
        input('Tecle ENTER para continuar')

    def _escolha_matriz(self, matrizes):
        print('Matrizes: ' + str(list(matrizes.keys())))
        k = input('Qual matriz? (Enter para nenhuma) ')
        if k == '':
            matriz = None
        else:
            matriz = matrizes[k]
        return matriz

    def _mostre_matriz(self, matriz):
        mostra_matriz(matriz, 5)
        print('Número de Linhas: {}'.format(matriz.num_linhas()))
        print('Número de Colunas: {}'.format(matriz.num_colunas()))
        linha = int(input('Digite uma linha: '))
        coluna = int(input('Digite uma coluna: '))
        nums_linha = matriz.linha(linha)
        nums_coluna = matriz.coluna(coluna)
        soma_linha = matriz.soma_de_linha(linha)
        soma_coluna = matriz.soma_de_coluna(coluna)
        somas_das_linhas = matriz.somas_das_linhas()
        soma_dos_numeros = matriz.soma_dos_numeros()
        print('Números da linha {} : {}'.format(linha, nums_linha))
        print('Números da coluna {} : {}'.format(coluna, nums_coluna))
        print('Soma da linha {} : {}'.format(linha, soma_linha))
        print('Soma da coluna {} : {}'.format(coluna, soma_coluna))
        print('Somas das linhas : {}'.format(somas_das_linhas))
        print('Soma dos números : {}'.format(soma_dos_numeros))
        fator = int(input('Fator de multiplicação: '))
        matriz.multiplique_por_fator(fator)
        mostra_matriz(matriz, 5)
        print('----------------------------------------------------')
