import string
import database
import json
import os
import crud
from bson import json_util

def writeAJson(data, name: str):
    parsed_json = json.loads(json_util.dumps(data))

    if not os.path.isdir("./json"):
        os.makedirs("./json")

    with open(f"./json/{name}.json", 'w') as json_file:
        json.dump(parsed_json, json_file,
                  indent=4,
                  separators=(',', ': '))

db = database.Database(database="Exercicios_BD2", collection="Livros")
db.resetDatabase()

crud = crud.LivroModel(db)

cthuluId = crud.create_livro("The call of Cthulu","H.P Lovecraft",1982,30.0)

crud.read_livro_by_id(cthuluId)

crud.update_livro(cthuluId,"Um deus anciao muiito louco e suas aventuras",2023)

crud.delete_livro(cthuluId)


