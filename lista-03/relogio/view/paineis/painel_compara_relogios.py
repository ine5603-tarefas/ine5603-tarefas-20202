# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Relógio
# --------------------------
# Classe que permite comparar dois relógios.
#

from model.relogio import Relogio

class PainelComparaRelogios:
    def compare(self, relogio):
        continuar = True
        while continuar:
            hms = relogio.hms()
            print('Relógio atual: {}:{}:{}'.format(hms[0], hms[1], hms[2]))
            print('-- Criando outro Relógio')
            hora = int(input('Hora: '))
            minuto = int(input('Minuto: '))
            segundo = int(input('Segundo: '))
            outro_relogio = Relogio(hora, minuto, segundo)
            resultado = relogio.compare_com(outro_relogio)
            if resultado == 0:
                print('Ambos marcam o mesmo horário!')
            elif resultado == -1:
                print('O relógio está atrasado em relação ao outro relógio!')
            else:
                print('O relógio está adiantado em relação ao outro relógio!')
            continuar = 's' == input('Criar outro relógio? [s/n]')