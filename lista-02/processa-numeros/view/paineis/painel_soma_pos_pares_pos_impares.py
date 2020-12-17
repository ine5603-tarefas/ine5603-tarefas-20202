# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por calcular a soma dos números em posições pares e ímpares de uma lista de números.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import soma_pos_pares_pos_impares

class PainelSomaPosParesPosImpares(PainelAbstrato):
    def __init__(self):
        super().__init__('Soma Posições Pares e Posições Ímpares')

    def interaja(self):
        numeros = self._leiaints()
        somas = soma_pos_pares_pos_impares(numeros)
        if somas is None:
            msg = 'Não dá para encontrar porque a lista {} tem menos de dois números'.format(numeros)
        else:
            msg = 'Para a lista {} a soma das posições pares é {} e das posições ímpares é {}.'.format(numeros, somas[0], somas[1])
        print(msg)
