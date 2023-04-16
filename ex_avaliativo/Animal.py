import Habitat as habt


class Animal:
    def __init__(self, nome: str, especie: str, idade: int, habitat: habt.Habitat):
        self.id = None
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat
