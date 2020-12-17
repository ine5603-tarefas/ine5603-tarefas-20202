# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe responsável pela interação com o usuário
#


from view.menu import Menu
from view.paineis.painel_soma import PainelSoma
from view.paineis.painel_em_posicoes_impares import PainelEmPosicoesImpares
from view.paineis.painel_primeiro_e_ultimo import PainelPrimeiroEUltimo
from view.paineis.painel_conta_ocorrencias import PainelContaOcorrencias
from view.paineis.painel_posicao_do_maior import PainelPosicaoDoMaior
from view.paineis.painel_maior import PainelMaior
from view.paineis.painel_qtd_acima_limite import PainelQtdAcimaDeLimite
from view.paineis.painel_media import PainelMedia
from view.paineis.painel_qtd_no_intervalo import PainelQtdNoIntervalo
from view.paineis.painel_multiplica_por_fator import PainelMultiplicaPorFator
from view.paineis.painel_multiplicado_por_fator import PainelMultiplicadoPorFator
from view.paineis.painel_n_primeiros import PainelNPrimeiros
from view.paineis.painel_copia import PainelCopia
from view.paineis.painel_no_intervalo import PainelNoIntervalo
from view.paineis.painel_una import PainelUna
from view.paineis.painel_pares import PainelPares
from view.paineis.painel_duplica import PainelDuplica
from view.paineis.painel_possui_par import PainelPossuiPar
from view.paineis.painel_primeira_posicao import PainelPrimeiraPosicao
from view.paineis.painel_posicoes import PainelPosicoes
from view.paineis.painel_sem_repeticoes import PainelSemRepeticoes
from view.paineis.painel_remove_ocorrencias import PainelRemoveOcorrencias
from view.paineis.painel_substitui_ocorrencias import PainelSubstituiOcorrencias
from view.paineis.painel_substitui_primeira_ocorrencia import PainelSubstituiPrimeiraOcorrencia
from view.paineis.painel_substitui_ultima_ocorrencia import PainelSubstituiUltimaOcorrencia
from view.paineis.painel_inverte import PainelInverte
from view.paineis.painel_soma_pos_pares_pos_impares import PainelSomaPosParesPosImpares
from view.paineis.painel_das_posicoes import PainelDasPosicoes
from view.paineis.painel_parte import PainelParte

class InterfaceComUsuario:
    def __init__(self):
        opcoes_g1 = {
            0 : ('Voltar', None),
            1 : ('Somar números', PainelSoma),
            2 : ('Em Posições Ímpares', PainelEmPosicoesImpares),
            3 : ('Primeiro e Último', PainelPrimeiroEUltimo),
            4 : ('Posição do Maior', PainelPosicaoDoMaior),
            5 : ('Maior', PainelMaior),
            6 : ('Média', PainelMedia),
            7 : ('Cópia', PainelCopia),
            8 : ('Pares', PainelPares),
            9 : ('Possui Par', PainelPossuiPar),
            10 : ('Duplica', PainelDuplica),
            11 : ('Sem Repetições', PainelSemRepeticoes),
            12 : ('Inverte', PainelInverte),
            13 : ('Soma Posições Pares e Posições Ímpares', PainelSomaPosParesPosImpares)
            }
            
        opcoes_g2 = {
            0 : ('Voltar', None),
            1 : ('Conta ocorrências', PainelContaOcorrencias),
            2 : ('Quantidade Acima de Limite', PainelQtdAcimaDeLimite),
            3 : ('Multiplica por Fator', PainelMultiplicaPorFator),
            4 : ('Multiplicado por Fator', PainelMultiplicadoPorFator),
            5 : ('Cópia dos N Primeiros', PainelNPrimeiros),
            6 : ('Primeira Posição de Número', PainelPrimeiraPosicao),
            7 : ('Posições de Número', PainelPosicoes),
            8 : ('Remove Número', PainelRemoveOcorrencias)
            }

        opcoes_g3 = {
            0 : ('Voltar', None),
            1 : ('Quantidade no Intervalo', PainelQtdNoIntervalo),
            2 : ('Números no Intervalo', PainelNoIntervalo),
            3 : ('Substitui Ocorrências', PainelSubstituiOcorrencias),
            4 : ('Substitui Primeira Ocorrência', PainelSubstituiPrimeiraOcorrencia),
            5 : ('Substitui Última Ocorrência', PainelSubstituiUltimaOcorrencia),
            6 : ('Parte', PainelParte)
        }

        opcoes_g4 = {
            0 : ('Voltar', None),
            1 : ('Unir duas Listas', PainelUna),
            2 : ('Números das Posições', PainelDasPosicoes)
        }

        menu_g1 = Menu('Lista de Números', opcoes_g1)
        menu_g2 = Menu('Lista de Números e 1 Número', opcoes_g2)
        menu_g3 = Menu('Lista de Números e 2 Números', opcoes_g3)
        menu_g4 = Menu('Duas Listas de Números', opcoes_g4)
        self._menu = Menu('Exercício Processa Números', {
            0 : ('Sair do Programa', None),
            1 : ('Só Lista de Números', menu_g1),
            2 : ('Lista de Números e 1 Número', menu_g2),
            3 : ('Lista de Números e 2 Números', menu_g3),
            4 : ('Duas Listas de Números', menu_g4)
        })

    def interaja(self):
        menu = self._menu.pergunte()
        while menu is not None:
            classe_painel = menu.pergunte()
            while classe_painel is not None:
                try:
                    classe_painel().execute()
                except Exception:
                    print('** Erro na execução!!')
                    input('Tecle <enter> para continuar')
                classe_painel = menu.pergunte()
            menu = self._menu.pergunte()
