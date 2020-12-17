# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por uma lista com números duplicados (2 vezes cada número).

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import duplica

class PainelDuplica(PainelAbstrato):
    def __init__(self):
        super().__init__('Duplica')

    def interaja(self):
        numeros = self._leiaints()
        duplicados = duplica(numeros)
        msg = 'A lista {} contém os seguintes números duplicados: {}'.format(numeros, duplicados)
        print(msg)
