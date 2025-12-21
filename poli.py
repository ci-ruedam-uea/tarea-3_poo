# Clase base
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")

# Clase hija 1
class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

# Clase hija 2
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla")

# Lista de objetos (polimorfismo)
animales = [Perro(), Gato(), Animal()]

# Recorremos la lista y llamamos al mismo método
for animal in animales:
    animal.hacer_sonido()
