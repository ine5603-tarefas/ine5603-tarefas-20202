# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Balde
# --------------------------
# Classe que representa um balde. Um balde é um objeto capaz de armazenar até N litros de água.
#

class Balde:
    def __init__(self, capacidade):
        '''Define a capacidade do balde que, inicialmente, está vazio.
        '''
        self._CAPACIDADE = capacidade
        self._quantidade = 0
        
    def fique_cheio(self):
        '''Faz com que o balde fique cheio.
        '''
        pass
        
    def fique_vazio(self):
        '''Faz com que o balde fique vazio.
        '''
        pass
        
    def esta_cheio(self):
        '''Verifica se o balde está cheio.
        
        Retorna True se estiver ou Falde caso contrário.
        '''
        return False
        
    def esta_vazio(self):
        '''Verifica se o balde está vazio.

        Retorna True se estiver ou False caso contrário.
        '''
        return False
    
    def capacidade(self):
        '''Retorna a capacidade do balde.
        '''
        return 88
    
    def quantidade(self):
        '''Retorna a quantidade de água no balde.
        '''
        return 13
    
    def derrame_em(self, outro_balde):
        '''Derrama, sem desperdiçar uma gota, a água em outro balde.
        '''
        pass

    def receba_de(self, outro_balde):
        '''Recebe, sem desperdiçar uma gota, a água existente em outro balde.
        '''
        pass