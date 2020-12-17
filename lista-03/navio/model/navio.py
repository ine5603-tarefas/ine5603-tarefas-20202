# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do Navio
# --------------------------
# Classe que representa um navio.
#

from model.container import Container

class Navio:
    def __init__(self, qtd_max_containers, peso_maximo):
        '''Um navio aceita uma quantidade máxima de containers e suporta um peso máximo (peso dos containers).
        Inicialmente o navio não transporta nenhum container.
        '''
        pass

    def capacidade(self):
        '''Retorna a capacidade do navio, ou seja, o número máximo de containers que pode transportar.
        '''
        return 25
    
    def peso_maximo(self):
        '''Retorna o peso máximo que o navio consegue transportar sem afundar.
        '''
        return 300
    
    def qtd_containers(self):
        '''Retorna quantos containers o navio está transportando.
        '''
        return 8
    
    def peso_transportado(self):
        '''Retorna o peso total dos containers que o navio está transportando.
        '''
        return 250
    
    def carregue(self, codigo, refrigerado, peso_mercadoria):
        '''Tenta carregar um container com determinado código, se é refrigerado (True)
        ou não (False) e o peso da mercadoria que está dentro do container para dentro do navio.
        Retorna True se conseguiu carregar ou False se não conseguiu. Motivos para não conseguir
        carregar: não tem mais espaço, o navio afundaria ou um container com o código informado
        já foi carregado.
        '''
        return True
        
    def descarregue(self, codigo):
        '''Tenta descarregar um container do navio a partir do seu código.
        Retorna ou o container que foi descarregado ou None para indicar que
        não havia container com o código informado.
        '''
        return Container('CT99', True, 900)
    
    def carregando(self, codigo):
        '''Retorna True se o navio estiver carregando um container com o código informado ou
        False caso contrário.
        '''
        return True
    
    def containers_abaixo_de_peso(self, peso):
        '''Retorna uma lista de containers cujo peso esteja abaixo do peso informado.
        '''
        return [ ]

