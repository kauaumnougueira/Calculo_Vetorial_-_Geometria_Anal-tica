from operacoes_vetoriais.Vetor import *

#ADIÇÂO
def adicao(vetor1, vetor2):
    result = [vetor_1 + vetor_2 for vetor_1, vetor_2 in zip(vetor1, vetor2)]
    return result

#SUBTRAÇÃO
def subtracao(vetor1, vetor2):
    result = [vetor_1 - vetor_2 for vetor_1, vetor_2 in zip(vetor1, vetor2)]
    return result

#PRODUTO ESCALAR
def prod_esc(vetor1, vetor2):
    result = [vetor_1 * vetor_2 for vetor_1, vetor_2 in zip(vetor1, vetor2)]
    result_esc = sum(result)
    return result_esc

#PRODUTO VETORIAL
def prod_vet():
    '''
    i j k i j
    x y z x y
    (jz - yk, kx - iz, iy - jx)
    '''