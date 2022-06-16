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
def prod_vet(vetor1, vetor2):
    '''
    0 1 2 0 1
    i j k i j
    x y z x y
    (jz - yk, kx - iz, iy - jx)
    '''
    vetor_aux1 = [vetor1[1] * vetor2[2], vetor1[2] * vetor2[0], vetor1[0] * vetor2[1]]
    vetor_aux2 = [vetor1[2] * vetor2[1], vetor1[0] * vetor2[2], vetor1[1] * vetor2[0]]
    result = [vetor_aux1 - vetor_aux2 for vetor_aux1, vetor_aux2 in zip(vetor_aux1, vetor_aux2)]
    return result