# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Jogo da Velha
# --------------------------
# Classe que permite criar um jogo da velha.
#

from model.jogador_humano import JogadorHumano
from model.jogador_maquina_aleatorio import JogadorMaquinaAleatorio
from model.jogo_da_velha import JogoDaVelha

class PainelCriaJogo():

    def crie(self, iu):
        print('- - - Criar Jogo da Velha - - -')
        jogadorHumano = self._crie_jogador_humano()
        jogadorMaquina = self._crie_jogador_maquina()
        print('Você jogará contra a máquina {}'.format(jogadorMaquina.nome()))
        quem_inicia = self._defina_quem_inicia(jogadorHumano.nome(), jogadorMaquina.nome())
        jogo = JogoDaVelha(humano=jogadorHumano, maquina=jogadorMaquina, inicia=quem_inicia)
        iu.armazene_jogo(jogo)
        print('Jogo definido!')
        input('Tecle ENTER para continuar')

    def _crie_jogador_humano(self):
        nome = input('Nome do jogador humano: ')
        return JogadorHumano(nome)

    def _crie_jogador_maquina(self):
        return JogadorMaquinaAleatorio()

    def _defina_quem_inicia(self, nomeHumano, nomeMaquina):
        inicia = input('Quem inicia o jogo? (h){} ou (m){} * [h, m] : '.format(nomeHumano, nomeMaquina))
        if inicia == 'h':
            inicia = 'humano'
        else:
            inicia = 'maquina'
        return inicia

