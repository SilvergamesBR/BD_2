import database

class CRUD:
    def __init__(self, database:database.Database):
        self.db = database

    def create(self, name, ano_nasc, cpf) :# cria um Teacher
        query = "CREATE (:Teacher{nome:$nome,ano_nasc:$ano_nasc,cpf:$cpf})"
        parameters = {"nome": name,"ano_nasc":ano_nasc,"cpf":cpf}
        return self.db.execute_query(query,parameters)

    def read(self, name) :# retorna apenas um Teacher
        query = "Match (t:Teacher{nome:$nome}) return t limit 1"
        parameters = {"nome":name}
        return self.db.execute_query(query,parameters)

    def delete(self, name): # deleta Teacher com base no name
        query = "Match (t:Teacher{nome:$nome}) detach delete t"
        parameters = {"nome": name}
        return self.db.execute_query(query, parameters)

    def update(self, name, newCpf): # atualiza cpf com base no nam
        query = "MATCH (t:Teacher{nome:$nome}) SET t.cpf = $cpf"
        parameters = {"nome":name,"cpf":newCpf}
        return self.db.execute_query(query,parameters)
