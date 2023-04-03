from pymongo import MongoClient
from bson.objectid import ObjectId


class SensorModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_sensor(self, nomeSensor: str, valorSensor: int, unidadeMedida: str, sensorAlarmado) -> str:
        try:
            result = self.collection.insert_one(
                {"nomeSensor": nomeSensor, "valorSensor": valorSensor, "unidadeMedida": unidadeMedida,
                 "sensorAlarmado": sensorAlarmado})
            sensor_id = str(result.inserted_id)
            print(f"Sensor {nomeSensor}  criado com id: {sensor_id}")
            return sensor_id
        except Exception as error:
            print(f"An error occurred while creating sensor: {error}")
            return None

    def update_sensor(self,sensor_Id : str, valorSensor : int, sensorAlarmado : bool) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(sensor_Id)}, {"$set": {"valorSensor": valorSensor, "sensorAlarmado": sensorAlarmado}})
            if result.modified_count:
                print(f"Livro {sensor_Id} atualizado com valor {valorSensor} e alarme {sensorAlarmado}")
            else:
                print(f"Nenhum sensor achado com {sensor_Id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating livro: {error}")
            return None
