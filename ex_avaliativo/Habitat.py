import Cuidador as cuid


class Habitat:
    def __init__(self, nome: str, tipoAmbiente: str, cuidador: cuid.Cuidador):
        self.id = None
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador
