# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por multiplicar os números de uma lista por um fator.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import multiplica_por_fator

class PainelMultiplicaPorFator(PainelAbstrato):
    def __init__(self):
        super().__init__('Multiplicar por Fator')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            fator = self._leia1int('Digite o fator : ')
            copia = numeros.copy()
            multiplica_por_fator(numeros, fator)
            print('A lista {} multiplicada pelo fator {} muda para {}.'.format(copia, fator, numeros))
            continuar = 's' == input('Outro fator? [s/n]')
