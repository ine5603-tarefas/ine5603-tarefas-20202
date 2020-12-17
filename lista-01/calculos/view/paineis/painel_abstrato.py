# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Classe que descreve o comportamento padrão de todo tipo de painel

from abc import ABC, abstractmethod

class PainelAbstrato(ABC):
    def __init__(self, titulo):
        self._titulo = titulo

    def execute(self):
        titulo = '- - - - {} - - - - '.format(self._titulo)
        outraVez = True
        while outraVez:
            print(titulo)
            self.interaja()
            outraVez = 's' == input('Outra vez? [s/n] :')
        print('- - - - Fim')

    @abstractmethod
    def interaja(self):
        pass

    def _leia3int(self):
        n1 = self._leia_int('Primeiro número: ')
        n2 = self._leia_int('Segundo número: ')
        n3 = self._leia_int('Terceiro número: ')
        return (n1, n2, n3)

    def _leia2int(self):
        n1 = self._leia_int('Primeiro número: ')
        n2 = self._leia_int('Segundo número: ')
        return (n1, n2)

    def _leia1int(self, msg='Digite um número: '):
        return self._leia_int(msg)

    def _leia_int(self, msg):
        numero = None
        while numero is None:
            try:
                numero = int(input(msg))
            except ValueError:
                print('Erro! Você deve digitar um número inteiro.')

        return numero

