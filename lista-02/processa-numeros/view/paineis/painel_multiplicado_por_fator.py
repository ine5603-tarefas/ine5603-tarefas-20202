# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por criar uma nova lista multiplicada por um fator.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import multiplicado_por_fator

class PainelMultiplicadoPorFator(PainelAbstrato):
    def __init__(self):
        super().__init__('Multiplicado por Fator')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            fator = self._leia1int('Digite o fator : ')
            multiplicado = multiplicado_por_fator(numeros, fator)
            print('A lista {} multiplicada pelo fator {} muda para {}.'.format(numeros, fator, multiplicado))
            continuar = 's' == input('Outro fator? [s/n]')
