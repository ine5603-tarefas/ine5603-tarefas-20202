# -------------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Matriz de Inteiros
# -------------------------------
# Classe que representa uma matriz de números inteiros.
#

class MatrizDeInteiros:
    def __init__(self, dimensoes_ou_numeros):
        '''Cria uma matriz de números inteiros. Há duas formas de criar:
        - passando as dimensões da matriz na forma de uma tupla: (número de linhas , número de colunas)
        - passando os números da matriz na forma de uma lista contendo listas de números
        '''
        if type(dimensoes_ou_numeros) is tuple:
            (num_linhas, num_colunas) = dimensoes_ou_numeros
            self._numeros = self._zeros(num_linhas, num_colunas)
        else:
            self._numeros = dimensoes_ou_numeros
            
    def _zeros(self, num_linhas, num_colunas):
        '''Gera uma lista de listas contendo zeros.
        '''
        return [ [0] * num_colunas for _ in range(num_linhas)]
    
    def armazene(self, linha, coluna, numero):
        '''Armazena um número na matriz em uma determinada posição (linha e coluna).
        Atenção: a primeira linha deve ser representada por 1. O mesmo vale para a
        primeira coluna.
        '''
        pass
        
    def obtenha(self, linha, coluna):
        '''Retorna o número que está em uma determinada posição (linha e coluna).
        Atenção: a primeira linha deve ser representada por 1. O mesmo vale para a
        primeira coluna.
        '''
        return 8
        
    def num_linhas(self):
        '''Retorna o número de linhas da matriz.
        '''
        return 6
    
    def num_colunas(self):
        '''Retorna o número de colunas da matriz.
        '''
        return 3
    
    def linha(self, linha):
        '''Retorna uma nova lista contendo os números que estão em uma linha.
        Atenção: a primeira linha deve ser representada por 1.
        '''
        return [3,4,5,6]

    def coluna(self, coluna):
        '''Retorna uma nova lista contendo os números que estão em uma coluna.
        Atenção: a primeira coluna deve ser representada por 1.
        '''
        return [9,8,7]

    def soma_de_linha(self, linha):
        '''Retorna a soma dos números que estão em uma linha da matriz.
        Atenção: a primeira linha deve ser representada por 1.
        '''
        return 77
    
    def soma_de_coluna(self, coluna):
        '''Retorna a soma dos números que estão em uma coluna da matriz.
        Atenção: a primeira coluna deve ser representada por 1.
        '''
        return 56
    
    def somas_das_linhas(self):
        '''Retorna uma lista contendo as somas de cada uma das linhas
        da matriz.
        '''
        return [ 23, 45, 77 ]
    
    def soma_dos_numeros(self):
        '''Retorna a soma de todos os números da matriz.
        '''
        return 99
    
    def multiplique_por_fator(self, fator):
        '''Multiplica cada número da matriz por um outro número (fator).
        '''
        pass

    def copia(self):
        '''Retorna uma cópia da matriz.
        '''
        return MatrizDeInteiros([[1,2,3], [4,5,6]])
    
    def __add__(self, outra):
        '''Faz a soma da matriz self com outra matriz.
        Retorna a matriz resultante da soma ou None quando
        não for possível somar.
        '''
        return None
        
    def __mul__(self, outra):
        '''Faz a multiplicação da matriz self com outra matriz.
        Retorna a matriz resultante da multiplicação ou None quando
        não for possível multiplicar.
        '''
        return None
            