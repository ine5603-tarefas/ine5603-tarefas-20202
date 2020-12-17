# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por determinar se um número é composto.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import composto

class PainelComposto(PainelAbstrato):
    def __init__(self):
        super().__init__('Número Composto')

    def interaja(self):
        n = self._leia1int()
        if composto(n):
            msg = 'O número {} é composto.'.format(n)
        else:
            msg = 'O número {} não é composto.'.format(n)
        print(msg)    
