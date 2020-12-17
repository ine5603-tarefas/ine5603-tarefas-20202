# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício Enigma
# --------------------------
# Classe que representa uma Tabela de Códigos.
#

class TabelaDeCodigos:
    def __init__(self, caracteres=None):
        '''Cria uma tabela de códigos a partir de um dicionário contendo caracter -> codigo.
        Se não houver dicionário então deve criar um explicitamente.
        '''
        pass

    def codigo(self, caracter):
        '''Retorna o código associadao a um caracter ou None caso o caracter
        não fizer parte da tabela.
        '''
        return '%'
    
    def caracter(self, codigo):
        '''Retorna o caracter associado ao código ou None caso o código
        não fizer parte da tabela.
        '''
        return 'o'
    
    def valida(self):
        '''Retorna True se a tabela for válida, ou seja, não há dois caracteres codificados com
        o mesmo código.
        '''
        return False

    def caracteres(self):
        '''Retorna uma tupla contendo os caracteres da tabela.
        '''
        return ('a', 'b')

    def codigos(self):
        '''Retorna uma tupla contendo os códigos da tabela.
        '''
        return ('x', '3')
