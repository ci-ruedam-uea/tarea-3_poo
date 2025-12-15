# ---------------------------------------------
# PROGRAMA: Promedio de notas de un estudiante
# ENFOQUE: Programación Tradicional
# ---------------------------------------------

# Función para ingresar las notas del estudiante
def ingresar_notas():
    # Lista donde se guardarán las notas
    notas = []

    # Pedimos al usuario cuántas notas va a ingresar
    cantidad = int(input("¿Cuántas notas desea ingresar?: "))

    # Ciclo para pedir cada nota
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)  # Se guarda la nota en la lista

    return notas


# Función para calcular el promedio
def calcular_promedio(notas):
    # Sumamos todas las notas
    suma = sum(notas)

    # Calculamos el promedio
    promedio = suma / len(notas)

    return promedio


# Función principal
def main():
    print("CÁLCULO DEL PROMEDIO - PROGRAMACIÓN TRADICIONAL\n")

    notas = ingresar_notas()           # Llamamos a la función para ingresar datos
    promedio = calcular_promedio(notas)  # Calculamos el promedio

    print(f"\nEl promedio final del estudiante es: {promedio:.2f}")


# Ejecutamos el programa
main()
