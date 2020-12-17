# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por determinar se dois números inteiros são amigos.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import amigos

class PainelAmigos(PainelAbstrato):
    def __init__(self):
        super().__init__('Números Amigos')

    def interaja(self):
        (n1, n2) = self._leia2int()
        if amigos(n1,n2):
            msg = 'Os números {} e {} são amigos.'.format(n1,n2)
        else:
            msg = 'Os números {} e {} não são amigos.'.format(n1,n2)
        print(msg)    
