class Cuidador:
    def __init__(self, nome: str, documento: str):
        self.id = None
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return self.nome