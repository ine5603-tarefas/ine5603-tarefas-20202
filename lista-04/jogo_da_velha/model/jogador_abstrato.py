# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que representa um jogador abstrato.
#

from abc import ABC, abstractmethod

class JogadorAbstrato(ABC):

    @abstractmethod
    def nome(self):
        '''Retorna o nome do jogador.
        '''
        pass
