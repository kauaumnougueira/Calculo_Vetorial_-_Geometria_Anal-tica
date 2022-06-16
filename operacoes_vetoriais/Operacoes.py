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
def prod_escalar(vetor1, vetor2):
    result = [vetor_1 * vetor_2 for vetor_1, vetor_2 in zip(vetor1, vetor2)]
    result_esc = sum(result)
    return result_esc

#PRODUTO VETORIAL
def prod_vetorial(vetor1, vetor2):
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

#PRODUTO MISTO
def prod_misto(vetor1, vetor2, vetor3):
    #VETOR1 X (VETOR3 X VETOR2)   
    result = prod_escalar(prod_vetorial(vetor3, vetor2), vetor1)
    return result

#PROJEÇÃO
def projecao(vetor1, vetor2):
    #DE VETOR1 EM VETOR2
    first_step = (prod_escalar(vetor1, vetor2)/ prod_escalar(vetor2, vetor2))
    result = [first_step * vetor2[0], first_step * vetor2[1], first_step * vetor2[2]]
    return result

