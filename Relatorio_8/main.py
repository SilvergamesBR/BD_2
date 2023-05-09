import database
import CRUD

db = database.Database("bolt://54.83.227.192:7687","neo4j","combustion-jam-walls")
db.drop_all()

CRUD  = CRUD.CRUD(db)

CRUD.create_player("XxrogerinxX")
CRUD.create_player("PedrinGameplays")
CRUD.create_player("PaoDeQueijoGamer")
CRUD.create_player("Pain Robertin")

players = ["XxrogerinxX","PedrinGameplays"]
CRUD.create_match("XxrogerinxX",players)

players.pop(0)
players.insert(0,"PaoDeQueijoGamer")
CRUD.create_match("PaoDeQueijoGamer",players)

players.pop(1)
players.insert(1,"Pain Robertin")
CRUD.create_match("Pain Robertin",players)

CRUD.create_relations()

print(CRUD.get_players())

CRUD.update_player("Pain Robertin","LOUD Robertin")
print(CRUD.get_players())

CRUD.delete_player("LOUD Robertin")
print(CRUD.get_players())

print(CRUD.get_match("Pain Robertin"))

print(CRUD.get_match_History("PaoDeQueijoGamer"))