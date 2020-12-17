# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por determinar o Máximo Divisor Comum entre dois números inteiros.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import mdc

class PainelMDC(PainelAbstrato):
    def __init__(self):
        super().__init__('Máximo Divisor Comum entre Dois Números')

    def interaja(self):
        (n1, n2) = self._leia2int()
        resultado = mdc(n1, n2)
        msg = 'O mdc entre {} e {} é {}'.format(n1,n2,resultado)
        print(msg)    
