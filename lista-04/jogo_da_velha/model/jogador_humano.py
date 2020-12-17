# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que representa um jogador humano
#

from model.jogador_abstrato import JogadorAbstrato

class JogadorHumano(JogadorAbstrato):
    def __init__(self, nome):
        '''Toda pessoa posui um nome.
        '''
        super().__init__()
        self._nome = nome

    def nome(self):
        '''Retorna o nome do jogador.
        '''
        return self._nome
    