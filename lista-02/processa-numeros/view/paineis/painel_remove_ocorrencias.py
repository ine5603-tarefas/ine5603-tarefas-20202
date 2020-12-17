# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por remover as ocorrências de um número.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import remove_ocorrencias

class PainelRemoveOcorrencias(PainelAbstrato):
    def __init__(self):
        super().__init__('Remove Ocorrências')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            numero = self._leia1int('Digite o número a ser removido : ')
            sem_numero = remove_ocorrencias(numeros, numero)
            print('A lista {} sem o número {} fica {}.'.format(numeros, numero, sem_numero))
            continuar = 's' == input('Outro número? [s/n]')
