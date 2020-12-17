# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Define funções usadas em vários painéis
#

def mostra_matriz(matriz, espacamento):
    '''Mostra os números de uma matriz com um
    espaçamento entre os números.
    '''
    mascara = '{0:' + str(espacamento) + '}'
    for l in range(1, matriz.num_linhas() + 1):
        nums = matriz.linha(l)
        snums = [mascara.format(n) for n in nums]
        print(''.join(snums))

