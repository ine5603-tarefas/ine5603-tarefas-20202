# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por multiplicar dois números inteiros.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import multiplica

class PainelMultiplica(PainelAbstrato):
    def __init__(self):
        super().__init__('Multiplica Dois Números')

    def interaja(self):
        (n1, n2) = self._leia2int()
        resultado = multiplica(n1, n2)
        msg = '{} * {} = {}'.format(n1,n2,resultado)
        print(msg)    
