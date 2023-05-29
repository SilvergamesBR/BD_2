import database
import queries

db = database.Database("bolt://3.83.179.171:7687","neo4j","stone-ages-peaks")
buscas = queries.CRUD(db)

opt = int(input("1 para buscar por labels, 2 para ver se duas pessoas sao irmas e\n3 para ver as pessoas com idade maior do que a indicada\n"))

while opt<1 or opt>3:
    opt = int(input("Por favor digite 1, 2 ou 3: "))

while opt>=1 and opt<=3:
    if opt == 1:
        label = input("Coloque a label por qual vc esta procurando: ")
        print(buscas.por_label(label))
    elif opt == 2:
        nome1 = input("Coloque o nome da primeira pessoa: ")
        nome2 = input("Coloque o nome da segunda pessoa: ")
        print(buscas.e_irmao(nome1,nome2))
    elif opt == 3:
        idade = int(input("Coloque a idade limite: "))
        print(buscas.idade_maior(idade))
    opt = int(input("coloque um numero diferente de 1, 2 ou 3 para parar, 1, 2 e 3 funcionam normalmente: "))