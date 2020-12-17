# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por contar as ocorrências de um número em uma lista.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import conta_ocorrencias

class PainelContaOcorrencias(PainelAbstrato):
    def __init__(self):
        super().__init__('Conta Ocorrências')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            numero = self._leia1int('Qual número? ')
            num_ocorrencias = conta_ocorrencias(numeros, numero)
            print('Na lista {} o número {} aparece {} vezes.'.format(numeros, numero, num_ocorrencias))
            continuar = 's' == input('Procurar outro número? [s/n]')
