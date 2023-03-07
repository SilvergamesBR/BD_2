import database
import json
import os
from bson import json_util
def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))


db = database.Database(database="Exercicios_BD2", collection="Pokedex")
db.resetDatabase()



bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")
