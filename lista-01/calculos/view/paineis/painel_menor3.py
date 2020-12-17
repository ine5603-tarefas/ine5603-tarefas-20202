# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por descobrir o menor de 3 números inteiros.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import menor_de_tres_numeros

class PainelMenor3(PainelAbstrato):
    def __init__(self):
        super().__init__('Menor de Três Números')

    def interaja(self):
        (n1, n2, n3) = self._leia3int()
        menor = menor_de_tres_numeros(n1,n2,n3)
        print('O menor entre {}, {} e {} é {}'.format(n1,n2,n3,menor))
