# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por verificar se lista possui número par.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import possui_par

class PainelPossuiPar(PainelAbstrato):
    def __init__(self):
        super().__init__('Possui Par')

    def interaja(self):
        numeros = self._leiaints()
        if possui_par(numeros):
            msg = 'A lista {} possui número par.'.format(numeros)
        else:
            msg = 'A lista {} não possui número par.'.format(numeros)
        print(msg)
