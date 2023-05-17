import database

class CRUD:
    def __init__(self, database:database.Database):
        self.db = database

    def por_label(self,label)#realiza um busca por todos os nos que contem uma label, no caso desse bc no geal as labelçs sao profissoes
        query = "match (n:"+label+") return n.nome"#o metodo pelos parameters tava dando erro, fiz na forca brutra mesmo
        return self.db.execute_query(query)

    def e_irmao(self,nome1,nome2):#reliza uma busca para ver se entre 2 nos com os campos nome passados por parametro tme um relacioanmento do time IRMAO_DE entre eles
        query = "match (p1:Pessoa{nome:$nome1})<-[i:IRMAO_DE]->(p2:Pessoa{nome:$nome2}) return i"
        parameters = {"nome1":nome1,"nome2":nome2}
        if self.db.execute_query(query, parameters):
            return True
        else:
            return False

    def idade_maior(self,idade):#realiza uma busca por todos os nos onde o campo idade e maior do que o numero passado por parametro
        query = "match (n) where n.idade > $idade return n.nome"
        parameters = {"idade":idade}
        return self.db.execute_query(query,parameters)