# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que representa um jogador máquina que faz jogadas aleatórias.
#

from random import randint
from model.jogador_abstrato import JogadorAbstrato

class JogadorMaquinaAleatorio(JogadorAbstrato):
    def __init__(self):
        super().__init__()

    def nome(self):
        '''Retorna o nome do jogador.
        '''
        return 'Jhonny Random'

    def faca_jogada(self, comecou_jogando, tabuleiro):
        '''Máquina faz a sua jogada no tabuleiro escolhendo aleatoriamente
        uma casa vazia.
        '''
        escolheu = False
        while not escolheu:
            linha = randint(1,3)
            coluna = randint(1,3)
            if comecou_jogando:
                escolheu = tabuleiro.marque_com_x(linha, coluna)
            else:
                escolheu = tabuleiro.marque_com_o(linha, coluna)

