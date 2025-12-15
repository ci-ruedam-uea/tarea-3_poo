# ---------------------------------------------------
# PROGRAMA: Promedio de notas de un estudiante
# ENFOQUE: Programación Orientada a Objetos (POO)
# ---------------------------------------------------

# ABSTRACCIÓN
# Clase base que representa a una persona en general
class Persona:
    def calcular_promedio(self):
        pass  # Método que será implementado por las clases hijas


# HERENCIA
# La clase Estudiante hereda de Persona
class Estudiante(Persona):

    # ENCAPSULACIÓN
    def __init__(self, nombre):
        self.nombre = nombre
        self.__notas = []  # Atributo privado

    # Método para ingresar las notas del estudiante
    def ingresar_notas(self):
        cantidad = int(input("¿Cuántas notas desea ingresar?: "))

        for i in range(cantidad):
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            self.__notas.append(nota)

    # POLIMORFISMO
    # Este método sobrescribe el de la clase Persona
    def calcular_promedio(self):
        suma = sum(self.__notas)
        promedio = suma / len(self.__notas)
        return promedio


# Función principal
def main():
    print("CÁLCULO DEL PROMEDIO - POO\n")

    nombre = input("Ingrese el nombre del estudiante: ")
    estudiante = Estudiante(nombre)

    estudiante.ingresar_notas()
    promedio = estudiante.calcular_promedio()

    print(f"\nEl promedio final de {estudiante.nombre} es: {promedio:.2f}")


# Ejecutamos el programa
main()
