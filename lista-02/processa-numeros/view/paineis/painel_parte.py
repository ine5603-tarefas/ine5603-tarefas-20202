# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por retornar uma parte da lista de números.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import parte

class PainelParte(PainelAbstrato):
    def __init__(self):
        super().__init__('Parte da Lista')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            pos = self._leia1int('Digite a posição onde inicia a parte: ')
            qtd = self._leia1int('Digite a quantidade de números da parte: ')

            if pos < 0 or qtd < 0:
                print('A posição e a quantidade devem ser pelo menos 0')
            else:
                a_parte = parte(numeros, pos, qtd)
                print('Na lista {} a parte que inicia em {} e tem tamanho {} é {}.'.format(numeros, pos, qtd, a_parte))
            continuar = 's' == input('Outra parte? [s/n]')
