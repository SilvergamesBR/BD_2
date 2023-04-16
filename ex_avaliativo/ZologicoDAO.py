from bson import ObjectId

import database
import Animal as anim
class ZoologicoDAO:
    def __init__(self):
        self.db = database.Database(database="Ex_avaliativo", collection="Animais")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def createAnimal(self,animal:anim.Animal):
        try:
            result = self.collection.insert_one({"nome": animal.nome, "especie": animal.especie,"idade": animal.idade,"habitat" : { "nome" : animal.habitat.nome, "tipoAmbiente": animal.habitat.tipoAmbiente, "cuidador": {"nome": animal.habitat.cuidador.nome, "documento": animal.habitat.cuidador.documento}}})
            animal.id = str(result.inserted_id)
            print(f"Animal {animal.nome}  criado com id: {animal.id} habitat: {animal.habitat} e cuidador {animal.habitat.cuidador}")
            return None
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")
            return None

    def readAnimal(self,id:str):
        try:
            animal = self.collection.find_one({"_id": ObjectId(id)})
            if animal:
                print(f"Animal achado: {animal}")
                return animal
            else:
                print(f"Nenhum livro achado com id:  {animal}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def updateAnimal(self,animal:anim.Animal):
        try:
            result = self.collection.update_one({"_id": ObjectId(animal.id)}, {"$set": {"nome": animal.nome, "especie": animal.especie,"idade": animal.idade,"habitat" : { "nome" : animal.habitat.nome, "tipoAmbiente": animal.habitat.tipoAmbiente, "cuidador": {"nome": animal.habitat.cuidador.nome, "documento": animal.habitat.cuidador.documento}}}})
            if result.modified_count:
                print(f"Animal {animal.id} atualizado com sucesso")
            else:
                print(f"Nenhum animal achado com {animal.id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def deleteAnimal(self, id:str):
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                print(f"Animal {id} deletado")
            else:
                print(f"Nenhum animal achado com id: {id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None