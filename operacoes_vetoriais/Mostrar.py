from operacoes_vetoriais.Operacoes import *


def to_see(x):
    if x == 2:
        print("-1 ADIÇÃO \n-2 SUBTRAÇÃO \n-3 PRODUTO ESCALAR \n-4 PRODUTO VETORIAL\n-5 PROJEÇÃO \n-6 MÓDULO DO PRODUTO VETORIAL")
        print("Escolha um ou mais operações (digite os numeros respectivos) (num num)")
        escolha = input()
        escolhido = escolha.split()
        return escolhido

    elif x == 3:
        print("-1 ADIÇÃO \n-2 SUBTRAÇÃO \n-3 PRODUTO MISTO")
        print("Escolha um ou mais operações (digite os numeros respectivos) (num num)")
        escolha = input()
        escolhido = escolha.split()
        return escolhido
        
def metodos_vetor_duplo(escolhido, vetor1, vetor2):
    i = 0
    for i in range(len(escolhido)):
        if escolhido[i] == '1':
            print(f"Adição do {vetor1} e {vetor2}: ", adicao(vetor1, vetor2))
        elif escolhido[i] == '2':
            print(f"Subtração do {vetor1} e {vetor2}: ", subtracao(vetor1, vetor2))
        elif escolhido[i] == '3':
            print(f"Produto escalar do {vetor1} e {vetor2}: ", prod_escalar(vetor1, vetor2))
        elif escolhido[i] == '4':
            print(f"Produto vetorial do {vetor1} e {vetor2}: ", prod_vetorial(vetor1, vetor2))
        elif escolhido[i] == '5':
            print(f"Projeção do {vetor1} sobre o {vetor2}: ", projecao(vetor1, vetor2))
        elif escolhido[i] == '6':
            print(f"Modulo do produto vetorial do {vetor1} e {vetor2}: ", modulo_prod_vet(vetor1, vetor2))
        else:
            print("Escolha não identificada")

def metodos_vetor_triplo(escolhido, vetor1, vetor2, vetor3):
    i = 0
    for i in range(len(escolhido)):
        if escolhido[i] == '1':
            print(f"Adição do {vetor1}, {vetor2} e {vetor3}: ", adicao(adicao(vetor1, vetor2), vetor3))
        elif escolhido[i] == '2':
            print(f"Subtração do {vetor1}, {vetor2} e {vetor3}: ", subtracao(subtracao(vetor1, vetor2), vetor3))
        elif escolhido[i] == '3':
            print(f"Produto misto do {vetor1}, {vetor2} e {vetor3}: ", prod_misto(vetor1, vetor2, vetor3))
        else:
            print("Escolha não identificada")                
