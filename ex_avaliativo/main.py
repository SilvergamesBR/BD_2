import Animal as anim
import Cuidador as cuid
import Habitat as habt
import ZologicoDAO as zoo

zoologico = zoo.ZoologicoDAO()
cuidador = cuid.Cuidador("Ze","123456")
habitat = habt.Habitat("savanaGrande","Savana",cuidador)
animal = anim.Animal("Leo","Leao",12,habitat)
zoologico.createAnimal(animal)
animal.nome = "Ruberio"
zoologico.updateAnimal(animal)
zoologico.deleteAnimal(animal.id)