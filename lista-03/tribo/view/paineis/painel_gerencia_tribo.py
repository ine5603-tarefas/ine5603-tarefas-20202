# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício da Tribo
# --------------------------
# Classe responsável por gerenciar os acontecimentos de uma tribo
#

from view.paineis.painel_abstrato import PainelAbstrato
from view.menu import Menu

class PainelGerenciaTribo(PainelAbstrato):

    def __init__(self, iu, tribo):
        super().__init__('Gerenciar Tribo {}'.format(tribo.nome()), iu)
        self._tribo = tribo

    def _interaja(self):
        opcoes = {
            0: 'Voltar',
            1: 'Mostrar Dados Gerais',
            2: 'Adicionar Guerreiro',
            3: 'Remover Guerreiro',
            4: 'Curar/Ferir Guerreiro',
            5: 'Exibir Guerreiro',
            6: 'Exibir Guerreiros vivos',
            7: 'Exibir Guerreiros mortos'
        }
        menu = Menu('Gerenciando', opcoes)
        voltar = False
        while not voltar:
            opcao = menu.pergunte()
            if opcao == 0:
                self._nao_continue()
                voltar = True
            elif opcao == 1:
                self._mostre_dados_gerais()
            elif opcao == 2:
                self._adicione_guerreiro()
            elif opcao == 3:
                self._remova_guerreiro()
            elif opcao == 4:
                self._cure_fira_guerreiro()
            elif opcao == 5:
                self._exiba_guerreiro()
            elif opcao == 6:
                self._exiba_vivos()
            elif opcao == 7:
                self._exiba_mortos()

    def _mostre_dados_gerais(self):
        print('** Dados Gerais da Tribo')
        print('Nome: {}'.format(self._tribo.nome()))
        print('Qtd Máxima Vidas de Guerreiro: {}'.format(self._tribo.max_vidas()))
        print('Qtd Máxima de Guerreiros: {}'.format(self._tribo.max_guerreiros()))
        qtd_vivos = self._tribo.qtd_vivos()
        qtd_mortos = self._tribo.qtd_mortos()
        qtd_guerreiros = self._tribo.qtd_guerreiros()
        print('Qtd Guerreiros: {} ({} vivos e {} mortos)'.format(qtd_guerreiros, qtd_vivos, qtd_mortos))
        print('***********************************************')
        input('Tele ENTER para continuar')

    def _adicione_guerreiro(self):
        print('** Adicionando Guerreiro')
        continuar = True
        while continuar:
            if self._tribo.qtd_guerreiros() == self._tribo.max_guerreiros():
                print('Não há mais espaço na tribo!')
                continuar = False
            else:
                nome = input('Nome do guerreiro: ')
                resultado = self._tribo.adicione_guerreiro(nome)    
                if resultado == 0:
                    print('Ok, adicionado.')
                elif resultado == 2:
                    print('Ops! Já existe guerreiro com este nome!')
                continuar = 's' == input('Adicionar outro? [s/n] ')

    def _remova_guerreiro(self):
        print('** Removendo Guerreiro')
        continuar = True
        while continuar:
            if self._tribo.qtd_guerreiros() == 0:
                print('Não há guerreiros na tribo!')
                continuar = False
            else:
                nome = input('Nome do guerreiro: ')
                removeu = self._tribo.remova_guerreiro(nome)    
                if removeu:
                    print('Ok, removido.')
                else:
                    print('Ops! Não existe guerreiro com este nome!')
                continuar = 's' == input('Remover outro? [s/n] ')                

    def _cure_fira_guerreiro(self):
        print('** Curando/Ferindo Guerreiro')
        if self._tribo.qtd_guerreiros() == 0:
            print('A tribo não possui guerreiros!')
        else:    
            continuar = True
            while continuar:
                nome = input('Nome do guerreiro: ')
                c_f = input('Curar ou Ferir? [c/f] : ')
                if c_f == 'c':
                    if self._tribo.cure(nome):
                        print('Guerreiro foi curado!')
                    else:
                        print('Não há guerreiro com este nome!')
                elif c_f == 'f':
                    if self._tribo.fira(nome):
                        print('Guerreiro foi ferido!')
                    else:
                        print('Não há guerreiro com este nome!')                
                continuar = 's' == input('Curar/Ferir outro? [s/n] ')                                

    def _exiba_guerreiro(self):
        print('** Exibindo Guerreiro')
        if self._tribo.qtd_guerreiros() == 0:
            print('A tribo não possui guerreiros!')
        else:    
            continuar = True
            while continuar:
                nome = input('Nome do guerreiro: ')
                self._mostre_guerreiro(nome, self._tribo.guerreiro(nome))
                continuar = 's' == input('Exibir outro? [s/n] ')   

    def _mostre_guerreiro(self, nome, g):
        if g is None:
            print('Não há guerreiro com o nome {}'.format(nome))   
        else:
            if g.esta_vivo():
                print('O guerreiro {} está vivo e ainda tem {} vida(s).'.format(nome, g.vidas()))
            else:
                print('O guerreiro {} está morto.'.format(nome))
        input('Tele ENTER para continuar')

    def _exiba_vivos(self):
        print('** Exibindo Guerreiros Vivos')
        vivos = self._tribo.vivos().values()
        if len(vivos) == 0:
            print('Não há guerreiros vivos')
        else:
            for g in vivos:
                print(g)
        input('Tele ENTER para continuar')


    def _exiba_mortos(self):
        print('** Exibindo Guerreiros Mortos')
        nomes_mortos = self._tribo.mortos().keys()
        if len(nomes_mortos) == 0:
            print('Não há guerreiros mortos')
        else:
            for nome in nomes_mortos:
                print(nome)
        input('Tele ENTER para continuar')
