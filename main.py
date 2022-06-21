from operacoes_vetoriais.Vetor import *
from operacoes_vetoriais.Operacoes import *
from operacoes_vetoriais.Mostrar import *

print("--------------------------------------")
print("Cálculo Vetorial e Geometria Analítica")
print("--------------------------------------")

print("Deseja operar quantos vetores?(2/3) ")
quant_vet = int(input(">"))

#RECEBENDO INPUTS DE 2 VETORES
print("Digite o vetor 1 (i j k): ")
aux1 = input(">")
aux1_vet = aux1.split()
vetor1 = Vetor(aux1_vet[0], aux1_vet[1], aux1_vet[2])

print("Digite o vetor 2 (i j k): ")
aux2 = input(">")
aux2_vet = aux2.split()
vetor2 = Vetor(aux2_vet[0], aux2_vet[1], aux2_vet[2])
    

#SE 3 VETORES
if quant_vet == 3: 
    print("Digite o vetor 3 (i j k): ")
    aux3 = input(">")
    aux3_vet = aux3.split()
    vetor3 = Vetor(aux3_vet[0], aux3_vet[1], aux3_vet[2])
    metodos_vetor_triplo(to_see(3), vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor(), vetor3.create_and_see_vetor())
elif quant_vet == 2:
    print() 
    metodos_vetor_duplo(to_see(2), vetor1.create_and_see_vetor(), vetor2.create_and_see_vetor())
else:
    print("ERRO")


