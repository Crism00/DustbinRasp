import Sensores
import ConexionMongo

CM = ConexionMongo();
S1 = Sensores();


data = S1.recibir();
jotason = S1.jotason(data);
CM.insertOne(jotason);