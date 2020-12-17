# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por obter os números pares.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import pares as encontra_pares

class PainelPares(PainelAbstrato):
    def __init__(self):
        super().__init__('Pares')

    def interaja(self):
        numeros = self._leiaints()
        pares = encontra_pares(numeros)
        msg = 'A lista {} contém os seguintes números pares: {}'.format(numeros, pares)
        print(msg)
