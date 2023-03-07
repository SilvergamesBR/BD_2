import string
import database
import json
import os
from bson import json_util

db = database.Database(database="Exercicios_BD2", collection="Pokedex")
db.resetDatabase()

def getPokemonByDex(number: int):
    return db.collection.find({"id": number})

def getPokemonByName(name: string):
    return db.collection.find({"name.english":name})

def getPokemonByType(type: string):
    return db.collection.find({"type": type})

def getPokemonByTypes(type1: string,type2: string):
    return db.collection.find({"type": [type1,type2]})

def getPokemonByAttribute(value: int,atribute: string, operation: string):
    return db.collection.find({("base."+atribute) : {("$"+operation): value}})

def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))





bulbasaur = getPokemonByDex(1)
writeAJson(bulbasaur, "bulbasaur")

charizard = getPokemonByName("Charizard")
writeAJson(charizard,"Charizard")

dragon = getPokemonByType("Dragon")
writeAJson(dragon,"DragonType")

flyingNdragon = getPokemonByTypes("Dragon","Flying")
writeAJson(flyingNdragon,"FlyingAndDragon")

lte50attack = getPokemonByAttribute(50,"Attack","lte")
writeAJson(lte50attack,"LessThan50Atk")

gte110speed = getPokemonByAttribute(110,"Speed","gte")
writeAJson(gte110speed,"MoreThan110Spd")