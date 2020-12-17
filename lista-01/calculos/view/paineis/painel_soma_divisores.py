# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável por calcular a soma dos divisores de um número inteiro.

from view.paineis.painel_abstrato import PainelAbstrato
from model.calculos import soma_dos_divisores

class PainelSomaDivisores(PainelAbstrato):
    def __init__(self):
        super().__init__('Soma dos Divisores')

    def interaja(self):
        n = self._leia1int()
        soma = soma_dos_divisores(n)
        msg = 'A soma dos divisores de {} é {}.'.format(n, soma)
        print(msg)    
