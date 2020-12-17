# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar as posições de um número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import posicoes_de_numero

class PainelPosicoes(PainelAbstrato):
    def __init__(self):
        super().__init__('Posições de Número')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            numero = self._leia1int('Digite o número : ')
            posicoes = posicoes_de_numero(numeros, numero)
            print('Na lista {} o número {} aparece nas posições {}.'.format(numeros, numero, posicoes))
            continuar = 's' == input('Outro número? [s/n]')
