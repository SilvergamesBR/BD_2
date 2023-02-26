import string


class Animal:
    nome: string
    idade: int
    especie: string
    cor: string
    som: string

    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor


class Elefante(Animal):
    tamanho: string
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho
        if(self.especie == 'Africano'):
            self.trombar()
            if(int(self.idade) < 10):
                self.tamanho = "Pequeno"
                self.som = "Paaah"
            else:
                self.tamanho = "grande"
                self.som = "PAHHHHHH"
            self.trombar()
            print(self.tamanho)

    def trombar(self):
        print(self.som)

    def mudar_tamanho(self, tamanho_novo):
        self.tamanho = tamanho_novo


a = Elefante(input("Digite o nome do elefante: "),input("Digite a idade do elefante: "),input("Digite a especie do elefante: "),input("Digite a cor do elefante: "),input("Digite o som do elefante: "),input("Digite o tamanho do elefante: "))