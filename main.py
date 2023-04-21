from Sensores import Sensor
import json
import time





S1 = Sensor()

while True:
# print(data)
    try:
        data = S1.recibir();
#     result = json.loads(data)
#     print(result)
#     S1.conexionMongo(result)
    except Exception as e:
        print(e);
            