# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar os números em posições ímpares.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import em_posicoes_impares

class PainelEmPosicoesImpares(PainelAbstrato):
    def __init__(self):
        super().__init__('Em Posições Ímpares')

    def interaja(self):
        numeros = self._leiaints()
        resposta = em_posicoes_impares(numeros)
        print('Para a lista {}'. format(numeros))
        print('Os números em posições ímpares são {}'. format(resposta))

