# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que permite gerenciar uma partida do jogo da velha.
#

class PainelGerenciaPartida:

    def gerencie(self, iu, jogo):
        marca_do_humano = jogo.marca_do_humano()
        marca_da_maquina = jogo.marca_da_maquina()
        nome_do_humano = jogo.nome_do_humano()
        nome_da_maquina = jogo.nome_da_maquina()
        while not jogo.terminou():
            if jogo.humano_deve_jogar():
                self._faca_humano_jogar(jogo, marca_do_humano, nome_do_humano)
            else:
                self._faca_maquina_jogar(jogo, marca_da_maquina, nome_da_maquina)
        self._mostre_resultado(jogo)
        iu.armazene_jogo(None)
        input('Tecle ENTER para terminar esta partida')


    def _faca_humano_jogar(self, jogo, marca, nome):
        print('-== {} Jogando ({}) ==-'.format(nome, marca))
        tabuleiro = jogo.tabuleiro()
        self._mostre_tabuleiro(tabuleiro)
        jogou = False
        while not jogou:
            linha = int(input('Linha [1,2,3]: '))
            coluna = int(input('Coluna [1,2,3]: '))
            jogou = jogo.registre_jogada_humana(linha, coluna)
            if not jogou:
                print('Casa já ocupada!')
        self._mostre_tabuleiro(tabuleiro)
        input('Tecle ENTER para continuar')


    def _faca_maquina_jogar(self, jogo, marca, nome):
        print('=__= {} Jogando ({}) =__='.format(nome,marca))
        print('Pensando...')
        jogo.faca_maquina_jogar()
        print('Jogou!')
        self._mostre_tabuleiro(jogo.tabuleiro())
        input('Tecle ENTER para continuar')

    def _mostre_tabuleiro(self, tabuleiro):
        casas = tabuleiro.copia_casas()
        print('-----')
        for i in range(3):
            print('|'.join(casas[i]))
        print('-----')   

    def _mostre_resultado(self, jogo):
        vencedor = jogo.vencedor()
        if vencedor is None:
            print('Ninguém venceu!')
        else:
            print('Jogador {} venceu!'.format(vencedor.nome()))

