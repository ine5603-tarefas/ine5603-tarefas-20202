# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por descobrir a soma de 3 números inteiros.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import soma_de_tres_numeros

class PainelSoma3(PainelAbstrato):
    def __init__(self):
        super().__init__('Soma de Três Números')

    def interaja(self):
        (n1, n2, n3) = self._leia3int()
        soma = soma_de_tres_numeros(n1,n2,n3)
        print('A soma de {}, {} e {} é {}'.format(n1,n2,n3,soma))

