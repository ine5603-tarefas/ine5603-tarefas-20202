# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por calcular a média dos números.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import media as calcula_media

class PainelMedia(PainelAbstrato):
    def __init__(self):
        super().__init__('Média')

    def interaja(self):
        numeros = self._leiaints()
        media = calcula_media(numeros)
        if media is None:
            msg = 'Não dá para encontrar porque a lista {} está vazia'.format(numeros)
        else:
            msg = 'Para a lista {} a média é {}.'.format(numeros, media)
        print(msg)
