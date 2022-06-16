from Operacoes import *

'''
1- PARALELOGRAMO (7)
2- TRIÂNGULO (13)
'''

#PARALELOGRAMO
def paralelogramo(vetor1, vetor2):
    area = modulo_prod_vet(vetor1, vetor2)
    return area

#TRIÂNGULO
def triangulo(vetor1, vetor2):
    area = modulo_prod_vet(vetor1, vetor2) / 2
    return area
