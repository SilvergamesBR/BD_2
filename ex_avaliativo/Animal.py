import Habitat as habt


class Animal:
    def __init__(self,id, nome: str, especie: str, idade: int, habitat: habt.Habitat):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat
