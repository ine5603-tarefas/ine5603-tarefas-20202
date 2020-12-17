# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício da Prefeitura
# --------------------------
# Funções que geram lista de objetos da classe Cidadao.
# 

from random import randrange
from model.cidadao import Cidadao

def gera_populacao_aleatoria(qtd=10000, menor_ano=1900, maior_idade=115, \
                             menor_renda=1200, incremento_renda=50, qtd_rendas=5):
    cidadaos = []
    for _ in range(qtd):
        ano_nascimento = menor_ano + randrange(maior_idade + 1)
        renda = menor_renda + incremento_renda * randrange(qtd_rendas)
        cidadaos.append(Cidadao(ano_nascimento, renda))
    return cidadaos


def gera_populacao_fixa():
    return [
        Cidadao(1923, 2000), 
        Cidadao(1987, 3000),
        Cidadao(1976, 2450),
        Cidadao(1982, 2300)
        ]
