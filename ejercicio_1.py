def suma(numeros, resultado = 0):
    for numero in numeros:
        if isinstance(numero, (int, float)):
            resultado = resultado + numero
        elif isinstance(numero, (list, tuple)):
            resultado = suma(numero, resultado)
    return resultado


numeros = [20, 10, 50.2, "25", "tres", [10, 10, "1", [1, 1, (8, 10)]], "cuatro", [1, "1", 9], (10, 10)]

print(suma(numeros))
