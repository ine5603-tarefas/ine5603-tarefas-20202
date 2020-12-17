# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por substituir a primeira ocorrência de um número por outro número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import substitui_primeira_ocorrencia

class PainelSubstituiPrimeiraOcorrencia(PainelAbstrato):
    def __init__(self):
        super().__init__('Substitui Primeira Ocorrência')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            substituido = self._leia1int('Digite o número a ser substituído: ')
            substituto = self._leia1int('Digite o número que ficará no lugar: ')
            original = numeros.copy()
            substitui_primeira_ocorrencia(numeros, substituido, substituto)
            print('A lista {} onde o {} foi trocado pelo {} fica {}.'.format(original, substituido, substituto, numeros))
            continuar = 's' == input('Outra substituição? [s/n]')
