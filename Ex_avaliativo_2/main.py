import database
import queries

db = database.Database("bolt://52.205.239.52:7687","neo4j","halves-benefits-desertion")
buscas = queries.CRUD(db)

print(buscas.quem_e_estudante())

print(buscas.e_irmao("Lucas","Elson"))
print(buscas.e_irmao("Lucas","Vanusa"))

print(buscas.idade_maior(20))