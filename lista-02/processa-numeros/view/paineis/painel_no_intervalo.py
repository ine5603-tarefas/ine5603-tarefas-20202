# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável por encontrar os números no intervalo.

from view.paineis.painel_abstrato import PainelAbstrato
from model.processa_numeros import no_intervalo

class PainelNoIntervalo(PainelAbstrato):
    def __init__(self):
        super().__init__('Números No Intervalo')

    def interaja(self):
        numeros = self._leiaints()
        continuar = True
        while continuar:
            limite_inf = self._leia1int('Digite o limite inferior do intervalo: ')
            limite_sup = self._leia1int('Digite o limite superior do intervalo: ')

            if limite_inf > limite_sup:
                print('o limite inferior ({}) deve ser menor ou igual ao limite superior ({})'.format(limite_inf, limite_sup))
            else:
                nums = no_intervalo(numeros, limite_inf, limite_sup)
                print('Na lista {} estão no intervalo[{}, {}] os números {}.'.format(numeros, limite_inf, limite_sup, nums))
            continuar = 's' == input('Outro intervalo? [s/n]')
