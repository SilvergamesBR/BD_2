import database

class CRUD:
    def __init__(self, database:database.Database):
        self.db = database

    def create_player(self,nome):
        query = "CREATE (:Player{nome:$nome})"
        parameters = {"nome": nome}
        self.db.execute_query(query,parameters)

    def create_match(self,winner,players):
        query = "CREATE (:Match{winner:$winner,players:$players})"
        parameters = {"winner":winner,"players":players}
        self.db.execute_query(query,parameters)

    def create_relations(self):
        query = "MATCH (p:Player),(m:Match{winner : p.nome}) CREATE (p)-[:GANHOU]->(m)"
        self.db.execute_query(query)
        query = "MATCH (p:Player),(m:Match) WHERE (p.nome in m.players) CREATE (p)-[:PARTICIPOU]->(m)"
        self.db.execute_query(query)

    def update_player(self,nomeAntigo,nomeNovo):
        query = "MATCH (p:Player{nome:$nomeantigo}) SET p.nome = $nomenovo"
        parameters = {"nomeantigo":nomeAntigo,"nomenovo":nomeNovo}
        self.db.execute_query(query,parameters)

    def delete_player(self,nome):
        query = "MATCH (p:Player{nome:$nome}) DETACH DELETE p"
        parameters = {"nome":nome}
        self.db.execute_query(query,parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p"
        return self.db.execute_query(query)

    def get_match(self,winner):
        query = "MATCH (m:Match{winner:$winner}) RETURN m"
        parameters = {"winner":winner}
        return self.db.execute_query(query,parameters)

    def get_match_History(self,player):
        query  = "MATCH (p:Player{nome:$player}),(m:Match) WHERE (p.nome in m.players) return m"
        parameters = {"player":player}
        return self.db.execute_query(query, parameters)