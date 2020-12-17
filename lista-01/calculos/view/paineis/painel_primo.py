# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por determinar se um número é primo.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import primo

class PainelPrimo(PainelAbstrato):
    def __init__(self):
        super().__init__('Número Primo')

    def interaja(self):
        n = self._leia1int()
        if primo(n):
            msg = 'O número {} é primo.'.format(n)
        else:
            msg = 'O número {} não é primo.'.format(n)
        print(msg)    
