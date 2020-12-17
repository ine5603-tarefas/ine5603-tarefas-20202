# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do Navio
# --------------------------
# Classe que permite mostra na tela os dados de um navio.
#

class PainelMostraNavio:

    def mostre(self, navio):
        pt = navio.peso_transportado()
        pm = navio.peso_maximo()
        perc_t = (pt / pm) * 100

        qt = navio.qtd_containers()
        capt = navio.capacidade()
        perc_qtd =  (qt / capt) * 100
        print('- - - Mostrar Navio - - -')
        print('Peso Transportado (Atual/Máximo/Percentual): {0} / {1} ({2:.2f}%)'.format(pt, pm, perc_t))
        print('Qtde Containers Transportados (Atual/Máximo): {0} / {1} ({2:.2f}%))'.format(qt, capt, perc_qtd))
        input('Digite ENTER para continuar')
