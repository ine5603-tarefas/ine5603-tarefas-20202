# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Balde
# --------------------------
# Classe que destroi os baldes criados.
#

from model.balde import Balde

class PainelDestroiBaldes:
    def destrua(self, iu):
        print('--- Destruir os Dois Baldes ---')
        destruir = 's' == input('Quer mesmo destruir os dois baldes? [s/n]')
        if destruir:
            iu.destrua_baldes()
