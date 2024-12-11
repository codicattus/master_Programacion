def calcular_area(*args):
    match args:
        case ("rectángulo", base, altura):
            return (f"Área del rectángulo: {base * altura}")
        case ("círculo", radio):
            return (f"Área del círculo: {3.14 * radio ** 2}")
        case ("triángulo", base, altura):
            return (f"Área del triángulo: {0.5 * base * altura}")
        case ("hexágono", perimetro, apotema):
            return (f"Área del hexágono: {perimetro * apotema / 2}")
        case _:
            return ("Figura desconocida")

area_rectangulo = calcular_area("rectángulo", 5, 3)
area_hexagono = calcular_area("hexágono", 18, 2.7)
print(area_rectangulo)
print(area_hexagono)
print(calcular_area("círculo", 4))


# Resultado:
#
# Área del rectángulo: 15
# Área del hexágono: 24.3
# Área del círculo: 50.24
