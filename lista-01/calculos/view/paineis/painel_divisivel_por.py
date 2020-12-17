# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por descobrir se um número inteiro é divisível por outro númeroo inteiro.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import divisivel_por

class PainelDivisivelPor(PainelAbstrato):
    def __init__(self):
        super().__init__('Número Divisível por Número')

    def interaja(self):
        (n1, n2) = self._leia2int()
        if divisivel_por(n1,n2):
            msg = '{} é divisível por {}'.format(n1,n2)
        else:
            msg = '{} não é divisível por {}'.format(n1,n2)
        print(msg)    
