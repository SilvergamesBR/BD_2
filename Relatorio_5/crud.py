from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_livro(self, titulo : str,autor: str, ano: int,preco : float ) -> str:
        try:
            result = self.collection.insert_one({"titulo": titulo, "autor": autor,"ano": ano,"preco" : preco})
            livro_id = str(result.inserted_id)
            print(f"Livro {titulo}  criado com id: {livro_id}")
            return livro_id
        except Exception as error:
            print(f"An error occurred while creating livro: {error}")
            return None

    def read_livro_by_id(self, livro_id: str) -> dict:
        try:
            livro = self.collection.find_one({"_id": ObjectId(livro_id)})
            if livro:
                print(f"Livro achado: {livro}")
                return livro
            else:
                print(f"Nenhum livro achado com id:  {livro_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading livro: {error}")
            return None

    def update_livro(self, livro_id: str, titulo: str, ano: int) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(livro_id)}, {"$set": {"titulo": titulo, "ano": ano}})
            if result.modified_count:
                print(f"Livro {livro_id} atualizado com titulo {titulo} e ano {ano}")
            else:
                print(f"Nenhum livro achado com {livro_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating livro: {error}")
            return None

    def delete_livro(self, livro_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(livro_id)})
            if result.deleted_count:
                print(f"Livro {livro_id} deletado")
            else:
                print(f"Nenhum livro achado com id: {livro_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting livro: {error}")
            return None