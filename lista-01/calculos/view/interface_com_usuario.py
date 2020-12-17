# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe responsável pela interação com o usuário

from view.menu import Menu
from view.paineis.painel_media3 import PainelMedia3
from view.paineis.painel_soma3 import PainelSoma3
from view.paineis.painel_par import PainelPar
from view.paineis.painel_menor3 import PainelMenor3
from view.paineis.painel_maior_que import PainelMaiorQue
from view.paineis.painel_divisivel_por import PainelDivisivelPor
from view.paineis.painel_multiplica import PainelMultiplica
from view.paineis.painel_divide import PainelDivide
from view.paineis.painel_bissexto import PainelBissexto
from view.paineis.painel_mdc import PainelMDC
from view.paineis.painel_soma_divisores import PainelSomaDivisores
from view.paineis.painel_amigos import PainelAmigos
from view.paineis.painel_primo import PainelPrimo
from view.paineis.painel_composto import PainelComposto


class InterfaceComUsuario:
    def __init__(self):
        opcoes = {
            0 : ('Sair do Programa', None),
            1 : ('Média de três números', PainelMedia3),
            2 : ('Soma de três números', PainelSoma3),
            3 : ('Menor de três números', PainelMenor3),
            4 : ('Número Par', PainelPar),
            5 : ('Maior que', PainelMaiorQue),
            6 : ('Divisível por', PainelDivisivelPor),
            7 : ('Multiplica', PainelMultiplica),
            8 : ('Divisão Inteira', PainelDivide),
            9 : ('Ano Bissexto', PainelBissexto),
            10 : ('Máximo Divisor Comum', PainelMDC),
            11 : ('Soma dos Divisores', PainelSomaDivisores),
            12 : ('Números Amigos', PainelAmigos),
            13 : ('Número Primo', PainelPrimo),
            14 : ('Número Composto', PainelComposto)
            }
        menu = Menu('Exercício Cálculos', opcoes)
        self._menu = menu

    def interaja(self):
        opcao = self._menu.pergunte()
        while opcao is not None:
            try:
                opcao().execute()
            except Exception:
                print('** Erro na execução!!')
                input('Tecle <enter> para continuar.')
            opcao = self._menu.pergunte()
