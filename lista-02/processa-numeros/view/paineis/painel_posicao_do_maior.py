# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar a posição do maior número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import posicao_do_maior

class PainelPosicaoDoMaior(PainelAbstrato):
    def __init__(self):
        super().__init__('Posição do Maior Número')

    def interaja(self):
        numeros = self._leiaints()
        posicao = posicao_do_maior(numeros)
        if posicao is None:
            msg = 'Não dá para encontrar porque a lista {} está vazia'.format(numeros)
        else:
            msg = 'Para a lista {} o maior número está na posição {}.'.format(numeros, posicao)
        print(msg)
