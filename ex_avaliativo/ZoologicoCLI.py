import ZoologicoDAO as DAO
import Animal as anim
import Habitat as habit
import Cuidador as cuid

class ZoologicoCLI:
    def __init__(self):
        self.dao = DAO.ZoologicoDAO()

    def menu(self):
        opcao = int(input("Digite 1 para inserir novos animais no BD, 2 para buscar os dados de um animal pelo seu ID,\n 3 para mudar os dados de um animal e 4 para apagar os dados de um animal,\n digite qualquer outro numero para fechar o programa: "))
        if opcao == 1 :
            self.createAnimal()
        elif opcao == 2 :
            self.readAnimal()
        elif opcao ==3 :
            self.updateAnimal()
        elif opcao == 4 :
            self.deleteAnimal()


    def createAnimal(self):
        print("Primeiro vamos registrar um cuidador para o animal !")
        nome = input("Qual e o nome desse cuidador ? ")
        documento = input("Ok, e qual e o documento do cuidador ? ")
        cuidador = cuid.Cuidador(nome,documento)
        print("Cuidador criado !")
        print("Agora vamos registrar os habitats pelos quais esse cuidador e responsavel !")
        habitats = []
        loop = 1
        while(loop == 1):
            idHabit = int(input("Qual vai ser o ID interno desse habitat ?(numeros apenas) "))
            nome = input("Qual vai ser o nome do habitat ? ")
            tipo = input("Qual e o tipo desse habitat ? ")
            habitat = habit.Habitat(idHabit,nome,tipo,cuidador)
            habitats.append(habitat)
            loop = int(input("1 para criar mais um habitat e qualquer outro numero para ir para registrar o animal "))
        print("Vamos agora registrar o animal ! ")
        nome = input("Qual e o nome do animal ? ")
        especie = input("Qual e a especie do animal ? ")
        idade = int(input("Qual e a idade do animal ?(apenas numeros) "))
        habitat = None
        while habitat == None:
            idHabit = int(input("Qual o id do habitat que sera utilizado ? "))
            for habi in habitats:
                if habi.id == idHabit:
                    habitat = habi
                    break

        animal = anim.Animal(None,nome,especie,idade,habitat)
        self.dao.createAnimal(animal)
        self.menu()

    #643f0f7e0e4071fa6526f777
    def readAnimal(self):
        id = input("Digite o id do animal: ")
        self.dao.readAnimal(id)
        self.menu()

    def updateAnimal(self):
        id = input("Digite o id do animal a ser atualizado: ")
        print("Vamos registrar um cuidador para o animal !")
        nome = input("Qual e o nome desse cuidador ? ")
        documento = input("Ok, e qual e o documento do cuidador ? ")
        cuidador = cuid.Cuidador(nome, documento)
        print("Cuidador criado !")
        print("Agora vamos registrar os habitats pelos quais esse cuidador e responsavel !")
        habitats = []
        loop = 1
        while (loop == 1):
            idHabit = int(input("Qual vai ser o ID interno desse habitat ?(numeros apenas) "))
            nome = input("Qual vai ser o nome do habitat ? ")
            tipo = input("Qual e o tipo desse habitat ? ")
            habitat = habit.Habitat(idHabit, nome, tipo, cuidador)
            habitats.append(habitat)
            loop = int(input("1 para criar mais um habitat e qualquer outro numero para ir para registrar o animal "))
        print("Vamos agora registrar o animal ! ")
        nome = input("Qual e o nome do animal ? ")
        especie = input("Qual e a especie do animal ? ")
        idade = int(input("Qual e a idade do animal ?(apenas numeros) "))
        habitat = None
        while habitat == None:
            idHabit = int(input("Qual o id do habitat que sera utilizado ? "))
            for habi in habitats:
                if habi.id == idHabit:
                    habitat = habi
                    break

        animal = anim.Animal(id, nome, especie, idade, habitat)
        self.dao.updateAnimal(animal)
        self.menu()


    def deleteAnimal(self):
        id = input("Digite o id do animal a ser apagado do BD: ")
        self.dao.deleteAnimal(id)