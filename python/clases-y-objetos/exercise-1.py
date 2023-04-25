class Vehículo:
    Color = "red"
    Ruedas = 4
    Puertas = 3

class Coche(Vehículo):
    Velocidad = 200
    Cilindrada = 1400

auto = Coche()

print(dir(auto))