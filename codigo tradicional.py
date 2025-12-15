# ---------------------------------------------
# PROMEDIO SEMANAL DEL CLIMA
# PROGRAMACIÓN TRADICIONAL
# ---------------------------------------------

# Función para ingresar las temperaturas
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


# Programa principal
def main():
    print("PROMEDIO SEMANAL DEL CLIMA - PROGRAMACIÓN TRADICIONAL\n")

    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)

    print(f"\nEl promedio semanal del clima es: {promedio:.2f} °C")


main()

