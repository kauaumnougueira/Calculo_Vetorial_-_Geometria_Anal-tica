class Vetor():

    #CONSTRUTOR DA CLASS VETOR
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
   
    #CRIA E MOSTRA UM VETOR
    def create_and_see_vetor(self):
        vetor = []
        vetor.append(self.i)
        vetor.append(self.j)
        vetor.append(self.k)
        int_vetor = list(map(int, vetor)) #TRANSFORMA EM INTEIRO
        return int_vetor
    

    
