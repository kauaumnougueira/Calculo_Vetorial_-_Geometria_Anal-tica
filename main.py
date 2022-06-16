from operacoes_vetoriais.Vetor import *
from operacoes_vetoriais.Operacoes import *

print("Cálculo Vetorial e Geometria Analítica")

#COM APENAS DOIS VETORES POR ENQUANTO
vetor1 = Vetor(1, 2, 3)
vetor2 = Vetor(4, 5, 6)

print(vetor1.create_and_see_vetor())
print(vetor2.create_and_see_vetor())

#PARA DOIS VETORES
print(adicao(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor()))
print(subtracao(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor()))
print(prod_escalar(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor()))
print(prod_vetorial(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor()))
print(projecao(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor()))
print(modulo_prod_vet(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor()))

#PARA TRES VETORES
vetor3 = Vetor(7, 8, 9)
print(prod_misto(vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor(), vetor3.create_and_see_vetor()))
