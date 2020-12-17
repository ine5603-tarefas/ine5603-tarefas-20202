# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por verificar se um ano é bissexto.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import bissexto

class PainelBissexto(PainelAbstrato):
    def __init__(self):
        super().__init__('Ano bissexto')

    def interaja(self):
        ano = self._leia1int('Digite um ano: ')
        if bissexto(ano):
            msg = 'O ano {} é bissexto.'.format(ano)
        else:
            msg = 'O ano {} não é bissexto.'.format(ano)
        print(msg)    
