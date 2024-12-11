def proceso_dato(dato):
    match dato:
        case ("rectángulo", base, altura):
            print(f"Área del rectángulo: {base * altura}")
        case ("círculo", radio):
            print(f"Área del círculo: {3.14 * radio ** 2}")
        case ("triángulo", base, altura):
            print(f"Área del triángulo: {0.5 * base * altura}")
        case _:
            print("Figura desconocida")

proceso_dato(("rectángulo", 5, 3))  # Salida: Área del rectángulo: 15
proceso_dato(("círculo", 4))       # Salida: Área del círculo: 50.24
proceso_dato(("triángulo", 6, 4))  # Salida: Área del triángulo: 12

