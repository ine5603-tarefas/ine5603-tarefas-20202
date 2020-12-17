# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por descobrir se um número inteiro é par.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import par

class PainelPar(PainelAbstrato):
    def __init__(self):
        super().__init__('Número Par')

    def interaja(self):
        n = self._leia1int()
        if par(n):
            msg = 'O número {} é par'.format(n)
        else:
            msg = 'O número {} não é par'.format(n)
        print(msg)

