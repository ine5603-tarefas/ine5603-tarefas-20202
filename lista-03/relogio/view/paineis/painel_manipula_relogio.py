# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Relógio
# --------------------------
# Classe que permite realiar diversas operações com um relógio.
#

from view.menu import Menu

class PainelManipulaRelogio:
    def manipule(self, relogio):
        opcoes = { 
            0: 'Voltar',
            1: 'Alterar Hora de Relógio',
            2: 'Alterar Minuto de Relógio',
            3: 'Alterar Segundo de Relógio',
            4: 'Alterar Hora, Minuto e Segundo de Relógio',
            5: 'Executar N ticks'
        }
        menu = Menu('Manipular Relógio', opcoes)
        self._mostra_relogio(relogio)
        opcao = menu.pergunte()
        while opcao != 0:
            if opcao == 1:
                print('-- Alterar Hora do Relógio')
                hora = int(input('Nova hora do relógio: '))
                relogio.mude_hora(hora)
            elif opcao == 2:
                print('-- Alterar Minuto do Relógio')
                minuto = int(input('Novo minuto do relógio: '))
                relogio.mude_minuto(minuto)
            elif opcao == 3:
                print('-- Alterar Segundo do Relógio')
                segundo = int(input('Novo segundo do relógio: '))
                relogio.mude_segundo(segundo)
            elif opcao == 4:
                print('-- Alterar Hora, Minuto e Segundo do relógio')
                hora = int(input('Nova hora do relógio: '))
                minuto = int(input('Novo minuto do relógio: '))
                segundo = int(input('Novo segundo do relógio: '))
                relogio.mude_hms(hora, minuto, segundo)
            elif opcao == 5:
                print('-- Executar N ticks no relógio')
                n = int(input('Quantos ticks: '))
                self._mostra_relogio(relogio)
                print('** iniciando ticks...')
                for _ in range(n):
                    print('Tick!')
                    relogio.tick()
                    self._mostra_relogio(relogio)
                print('** fim de ticks')

            self._mostra_relogio(relogio)
            opcao = menu.pergunte()

    def _mostra_relogio(self, relogio):
        hms = relogio.hms()
        msg = '{}:{}:{}'.format(hms[0], hms[1], hms[2])
        print('Relógio:')
        print(msg)
        print('======================')
