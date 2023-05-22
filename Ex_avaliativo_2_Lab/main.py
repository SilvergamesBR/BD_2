import teacherCRUD
import database

db = database.Database("bolt://44.199.249.152:7687","neo4j","cosals-desk-chests")
CRUD = teacherCRUD.CRUD(db)

db.drop_all()

print(CRUD.create('Chris Lima',1956,'189.052.396-66'))

print(CRUD.read("Chris Lima"))

print(CRUD.update("Chris Lima","162.052.777-77"))