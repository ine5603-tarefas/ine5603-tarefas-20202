# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar o maior número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import maior as acha_maior

class PainelMaior(PainelAbstrato):
    def __init__(self):
        super().__init__('Maior Número')

    def interaja(self):
        numeros = self._leiaints()
        maior = acha_maior(numeros)
        if maior is None:
            msg = 'Não dá para encontrar porque a lista {} está vazia'.format(numeros)
        else:
            msg = 'Para a lista {} o maior número é o {}.'.format(numeros, maior)
        print(msg)
