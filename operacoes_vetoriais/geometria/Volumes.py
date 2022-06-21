from operacoes_vetoriais.Operacoes import * 

'''
1- TETRAEDRO (7)
'''

#TETRAEDRO
def tetraedro(vetor1, vetor2, vetor3):
    prod = prod_misto(vetor1, vetor2, vetor3)
    volume = prod * 1/6
    return volume