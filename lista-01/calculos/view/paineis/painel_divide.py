# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por fazer a divisão inteira dois números inteiros.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import divide

class PainelDivide(PainelAbstrato):
    def __init__(self):
        super().__init__('Divisão Inteira de Dois Números')

    def interaja(self):
        (n1, n2) = self._leia2int()
        resultado = divide(n1, n2)
        msg = '{} // {} = {}'.format(n1,n2,resultado)
        print(msg)    
