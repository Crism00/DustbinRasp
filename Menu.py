import Sensores

S1 = Sensores();
data = S1.recibir();
jotason = S1.jotason(data);
S1.conexionMongo(jotason);