# ---------------------------------------------------
# PROMEDIO SEMANAL DEL CLIMA
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# ---------------------------------------------------

# ABSTRACCIÓN
class Clima:
    def calcular_promedio(self):
        pass


# HERENCIA
class ClimaSemanal(Clima):

    # ENCAPSULACIÓN
    def __init__(self):
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.__temperaturas.append(temp)

    # POLIMORFISMO
    def calcular_promedio(self):
        total = sum(self.__temperaturas)
        promedio = total / len(self.__temperaturas)
        return promedio


def main():
    print("PROMEDIO SEMANAL DEL CLIMA - POO\n")

    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print(f"\nEl promedio semanal del clima es: {promedio:.2f} °C")


main()
