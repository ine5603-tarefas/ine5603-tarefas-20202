# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por obter uma cópia dos N primeiros números.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import n_primeiros

class PainelNPrimeiros(PainelAbstrato):
    def __init__(self):
        super().__init__('N Primeiros')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            n = self._leia1int('Copiar quantos? ')
            copia = n_primeiros(numeros, n)
            print('Na lista {} a cópoia dos {} primeiros é a lista {}.'.format(numeros, n, copia))
            continuar = 's' == input('Outra quantidade? [s/n]')
