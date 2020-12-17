# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por contar quantos números estão acima de um limite.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import qtd_acima_limite

class PainelQtdAcimaDeLimite(PainelAbstrato):
    def __init__(self):
        super().__init__('Quantos Acima de Limite')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            limite = self._leia1int('Digite o limite : ')
            qtd = qtd_acima_limite(numeros, limite)
            print('Na lista {} há {} números acima do limite {}.'.format(numeros, qtd, limite))
            continuar = 's' == input('Outro limite? [s/n]')
