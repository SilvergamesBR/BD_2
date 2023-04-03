import random
import threading
import time
import database
import crud

class Sensor:
    valorSensor : int
    unidadeMedida : str
    sensorAlarmado : bool
    nomeSensor : str
    sensor_id : str
    def __init__(self, nomeSensor : str ,crud : crud.SensorModel):
        self.nomeSensor = nomeSensor
        self.valorSensor = random.randrange(30,41)
        self.unidadeMedida = "C"
        self.sensorAlarmado = False
        self.sensor_id = crud.create_sensor(nomeSensor,self.valorSensor,self.unidadeMedida,self.sensorAlarmado)

    def startUpdating(self,crud : crud.SensorModel):
        x = threading.Thread(target = sensorUpdate,args = (self,crud))
        x.start()

def sensorUpdate(sensor : Sensor, crud : crud.SensorModel):
    flag = True
    while flag:
        temp = random.randrange(30,41)
        if temp > 38:
            alarm = True
            flag = False
            print(f"Atencao ! Temperatura muito alta, verificar sensor {sensor.nomeSensor} !")
        else:
            alarm = False
        crud.update_sensor(sensor.sensor_id, temp, alarm)
        time.sleep(2)





db = database.Database(database="bancoiot", collection="sensores")
db.resetDatabase()
crud = crud.SensorModel(db)
sensor = Sensor("1",crud)
sensor.startUpdating(crud)
sensor2 = Sensor("2",crud)
sensor2.startUpdating(crud)
sensor3 = Sensor("3",crud)
sensor3.startUpdating(crud)



