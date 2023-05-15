import database

class CRUD:
    def __init__(self, database:database.Database):
        self.db = database

    def quem_e_estudante(self):
        query = "match (n:Estudante) return n.nome"
        return self.db.execute_query(query)

    def e_irmao(self,nome1,nome2):
        query = "match (p1:Pessoa{nome:$nome1})<-[i:IRMAO_DE]->(p2:Pessoa{nome:$nome2}) return i"
        parameters = {"nome1":nome1,"nome2":nome2}
        if self.db.execute_query(query, parameters):
            return True
        else:
            return False

    def idade_maior(self,idade):
        query = "match (n) where n.idade > $idade return n.nome"
        parameters = {"idade":idade}
        return self.db.execute_query(query,parameters)