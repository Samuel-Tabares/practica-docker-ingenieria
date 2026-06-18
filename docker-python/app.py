def calcular_potencia():
    try:
        base = float(input("Ingrese la base (b): "))
        exponente = int(input("Ingrese el exponente entero (e): "))

        if exponente < 0:
            print("Error: El exponente debe ser un entero no negativo.")
            return

        resultado = base ** exponente
        print(f"Resultado Exitoso: {base} elevado a la {exponente} es = {resultado}")
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar números válidos.")

def main():
    print("=== CALCULADORA DE POTENCIA EN DOCKER (PYTHON v2) ===")
    while True:
        calcular_potencia()
        opcion = input("\n¿Desea realizar otro cálculo? (Enter = sí / 'salir' = terminar): ").strip().lower()
        if opcion == "salir":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        print()

if __name__ == "__main__":
    main()
