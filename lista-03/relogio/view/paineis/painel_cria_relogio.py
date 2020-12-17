# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Relógio
# --------------------------
# Classe que permite a criação de relógio
#

from model.relogio import Relogio

class PainelCriaRelogio:

    def crie(self, tipo, iu):
        print('--- Criar Relógio ---')
        if tipo == 'h':
            print('Criando relógio apenas com a hora')
            hora = int(input('Hora: '))
            relogio = Relogio(hora=hora)
        elif tipo == 'm':
            print('Criando relógio apenas com o minuto')
            minuto = int(input('Minuto: '))
            relogio = Relogio(minuto=minuto)
        elif tipo == 's':
            print('Criando relógio apenas com o segundo')
            segundo = int(input('Segundo: '))
            relogio = Relogio(segundo=segundo)
        elif tipo == 'hm':
            print('Criando relógio apenas com hora e minuto')
            hora = int(input('Hora: '))
            minuto = int(input('Minuto: '))
            relogio = Relogio(hora=hora, minuto=minuto)
        elif tipo == 'hs':
            print('Criando relógio apenas com hora e segundo')
            hora = int(input('Hora: '))
            segundo = int(input('Segundo: '))
            relogio = Relogio(hora=hora, segundo=segundo)
        elif tipo == 'ms':
            print('Criando relógio apenas com minuto e segundo')
            minuto = int(input('Minuto: '))
            segundo = int(input('Segundo: '))
            relogio = Relogio(minuto=minuto, segundo=segundo)
        elif tipo == 'hms':
            print('Criando relógio com hora, minuto e segundo')
            hora = int(input('Hora: '))
            minuto = int(input('Minuto: '))
            segundo = int(input('Segundo: '))
            relogio = Relogio(hora=hora, minuto=minuto, segundo=segundo)
        else:
            relogio = Relogio()
        iu.armazene_relogio(relogio)
