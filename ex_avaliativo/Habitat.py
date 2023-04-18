import Cuidador as cuid


class Habitat:
    def __init__(self,id: int ,nome: str, tipoAmbiente: str, cuidador: cuid.Cuidador):
        self.id = id
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador

    def __str__(self):
        return self.nome