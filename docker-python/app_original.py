import sys

def calcular_potencia():
    print("=== CALCULADORA DE POTENCIA EN DOCKER (PYTHON) ===")
    try:
        base = float(input("Ingrese la base (b): "))
        exponente = int(input("Ingrese el exponente entero (e): "))

        if exponente < 0:
            print("Error: El exponente debe ser un entero no negativo.")
            return

        resultado = base ** exponente
        print(f"\nResultado Exitoso: {base} elevado a la {exponente} es = {resultado}")
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar números válidos.")

if __name__ == "__main__":
    calcular_potencia()
