import string
import database
import json
import os
from bson import json_util

def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))

db = database.Database(database="Exercicios_BD2", collection="Relatorio_4")
db.resetDatabase()

comprasB = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$match": { "cliente_id": "B" }},
    {"$group": {"_id": "B", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
])

menosVendido = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group":{"_id": "$produtos.nome","total":{"$sum":"$produtos.quantidade"}}},
    {"$sort": {"total":1}},
    {"$group": {"_id": None,"produtoMenosVendido":{"$first":"$_id"}}}
])

menosGastou = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group":{"_id": "$cliente_id","totalGasto":{"$sum":{"$multiply":["$produtos.quantidade","$produtos.preco"]}}}},
    {"$sort":{"totalGasto":1}},
    {"$group": {"_id": None ,"clienteMenosGastou":{"$first":"$_id"}}}
])

maisQ2 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group":{"_id": "$produtos.nome","total":{"$sum":"$produtos.quantidade"}}},
    {"$match": {"total": {"$gte":3}}}
])

writeAJson(comprasB,"ComprasB")
writeAJson(menosVendido,"MenosVendido")
writeAJson(menosGastou,"MenosGastou")
writeAJson(maisQ2,"VendeuMaisQ2")

