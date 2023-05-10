import pickle


class Vehiculo:
    def __init__(self, marca, vehiculo, color):
        self.marca = marca
        self.vehiculo = vehiculo
        self.color = color

    def __str__(self):
        return f"marca: {self.marca}, vehiculo: {self.vehiculo}, color: {self.color}"


auto = Vehiculo("Ford", "Taunus", "Dorado")

w = open("datos.bin", "wb")

pickle.dump(auto, w)

w.close()

with open("datos.bin", "rb") as r:
    auto_cargado = pickle.load(r)

print(auto_cargado)
