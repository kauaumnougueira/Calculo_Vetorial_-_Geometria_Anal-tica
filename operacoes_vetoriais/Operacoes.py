from math import math
'''
FUNÇÕES DE OPEAÇÕES DE VETORES
-1 ADIÇÃO (15)
-2 SUBTRAÇÃO (20)
-3 PRODUTO ESCALAR (25)
-4 PRODUTO VETORIAL (31)
-5 PRODUTO MISTO (38)
-6 PROJEÇÃO (44)
-7 MÓDULO DO PRODUTO VETORIAL (51)
'''


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

#MÓDULO DO PRODUTO VETORIAL
def modulo_prod_vet(vetor1, vetor2):
    pot1 = [vetor1[0] ** 2, vetor1[1] ** 2, vetor1[2] ** 2]
    pot2 = [vetor2[0] ** 2, vetor2[1] ** 2, vetor2[2] ** 2]
    result = math.sqr(sum(pot1)) * math.sqr(sum(pot2)) 
    return result