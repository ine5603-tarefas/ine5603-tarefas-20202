# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por inverter os números de uma lista.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import inverte

class PainelInverte(PainelAbstrato):
    def __init__(self):
        super().__init__('Inverte')

    def interaja(self):
        numeros = self._leiaints()
        invertidos = inverte(numeros)
        msg = 'A lista {} invertida fica {}'.format(numeros, invertidos)
        print(msg)
