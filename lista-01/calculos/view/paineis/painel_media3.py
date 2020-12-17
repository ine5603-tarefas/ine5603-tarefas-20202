# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por descobrir a média de 3 números inteiros.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import media_de_tres_numeros

class PainelMedia3(PainelAbstrato):
    def __init__(self):
        super().__init__('Média de Três Números')

    def interaja(self):
        (n1, n2, n3) = self._leia3int()
        media = media_de_tres_numeros(n1,n2,n3)
        print('A média de {}, {} e {} é {}'.format(n1,n2,n3,media))
