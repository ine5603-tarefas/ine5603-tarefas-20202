# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por descobrir se um número inteiro é maior que outro númeroo inteiro.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import maior_que

class PainelMaiorQue(PainelAbstrato):
    def __init__(self):
        super().__init__('Número Maior que Número')

    def interaja(self):
        (n1, n2) = self._leia2int()
        if maior_que(n1,n2):
            msg = '{} é maior que {}'.format(n1,n2)
        else:
            msg = '{} não é maior que {}'.format(n1,n2)
        print(msg)    
