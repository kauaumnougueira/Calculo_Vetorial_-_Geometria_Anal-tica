from Operacoes import *

#PARALELOGRAMO
def paralelogramo(vetor1, vetor2):
    area = modulo_prod_vet(vetor1, vetor2)
    return area

#TRIÂNGULO
def triangulo(vetor1, vetor2):
    area = modulo_prod_vet(vetor1, vetor2) / 2
    return area
