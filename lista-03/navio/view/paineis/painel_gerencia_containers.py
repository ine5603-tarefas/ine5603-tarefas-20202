# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício do Navio
# --------------------------
# Classe que permite gerenciar os containers de um navio.
#

from view.menu import Menu

class PainelGerenciaContainer:

    def gerencie(self, navio):
        opcoes = {
            0: 'Voltar',
            1: 'Carregar Container',
            2: 'Descarregar Container',
            3: 'Verificar se Carrega Container',
            4: 'Procurar Containers por Peso'
        }
        menu = Menu('Gerenciando Containers', opcoes)
        voltar = False
        while not voltar:
            opcao = menu.pergunte()
            if opcao == 0:
                voltar = True
            else:
                if opcao == 1:
                    self._carregue(navio)
                elif opcao == 2:
                    self._descarregue(navio)
                elif opcao == 3:
                    self._verifique(navio)
                elif opcao == 4:
                    self._procure_por_peso(navio)

    def _carregue(self, navio):
        print('** Carregar Container **')
        codigo = input('Código do Container: ')
        refrigerado = 'S' == input('Refrigerado? [s/n]').upper()
        peso_mercadoria = int(input('Peso da mercadoria: '))
        if navio.carregue(codigo, refrigerado, peso_mercadoria):
            print('Carregou!')
        else:
            print('Não foi possível carregar.')
        input('Tecle ENTER para continuar')

    def _descarregue(self, navio):
        print('** Descarregar Container **')
        codigo = input('Código do Container a ser descarregado: ')
        container = navio.descarregue(codigo)
        if container is None:
            print('Não há container com código {}'.format(codigo))
        else:
            print('Descarregado container {} cujo peso é {}'.format(codigo, container.peso()))
        input('Tecle ENTER para continuar')

    def _verifique(self, navio):
        print('** Verificar se Carrega Container **')
        codigo = input('Código do Container a ser verificado: ')
        if navio.carregando(codigo):
            print('Sim, está carregando este container.')
        else:
            print('Não, não carrega este container.')
        input('Tecle ENTER para continuar')

    def _procure_por_peso(self, navio):
        print('** Procurar Conainers Mais Leves Que **')
        peso = int(input('Qual o peso limite desejado? '))
        containers = navio.containers_abaixo_de_peso(peso)
        if len(containers) == 0:
            print('Não há nenhum container cujo peso esteja abaixo de {}'.format(peso))
        else:
            print('Há {} container(s) cujo peso está abaixo de {}'.format(len(containers), peso))
            for container in containers:
                print(container)
        input('Tecle ENTER para continuar')

