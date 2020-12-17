# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe que representa um guerreiro.
#

class Guerreiro:
    def __init__(self, nome, max_vidas):
        '''Cria um guerreiro sabendo-se o seu nome e o número máximo de vidas que pode ter.
        Inicialmente possui todas as vidas.
        '''
        pass

    def __str__(self):
        '''Retorna str mostrando o nome e o número de vidas do guerreiro.
        '''
        return 'nome:' + 'Barba Negra' + ' vidas:' + str(18)
        
    def nome(self):
        '''Retorna o nome do guerreiro.
        '''
        return 'Pena Grande'
    
    def max_vidas(self):
        '''Retorna o número máximo de vidas do guerreiro.
        '''
        return 6
    
    def vidas(self):
        '''Retorna o número de vidas do guerreiro.
        '''
        return 3
    
    def esta_vivo(self):
        '''Retorna True se guerreiro está vivo (tem pelo menos 1 vida) ou 
        False caso contrário.
        '''
        return True
    
    def perca_vida(self):
        '''Diminui uma vida do guerreiro.
        Atenção: ninguém pode ter menos de zero vidas.
        '''
        pass

    def ganhe_vida(self):
        '''Aumenta uma vida do guerreiro.
        Atenção:  ninguém pode ter mais vidas que o máximo de vidas.
        '''
        pass
            
    def copia(self):
        '''Retorna uma cópia do guerreiro.
        '''
        copia = Guerreiro('Rio Grande', 8)
        return copia

