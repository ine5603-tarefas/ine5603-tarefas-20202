# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar posição da primeira ocorrência de um número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import primeira_posicao_de_numero

class PainelPrimeiraPosicao(PainelAbstrato):
    def __init__(self):
        super().__init__('Primeira Posição de Número')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            numero = self._leia1int('Digite o número : ')
            posicao = primeira_posicao_de_numero(numeros, numero)
            if posicao is None:
                msg = 'O número {} não está na lista {}.'.format(numero, numeros)
            else:
                msg = 'O número {} aparece na posição {} na lista {}.'.format(numero, posicao, numeros)
            print(msg)
            continuar = 's' == input('Outro número? [s/n]')
