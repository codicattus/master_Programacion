# Aplica una función a todos los elementos de un iterable.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_celsius = [0, 20, 30, 100]
temperaturas_fahrenheit = list(map(celsius_a_fahrenheit, temperaturas_celsius))

print(temperaturas_fahrenheit)  

# Resultado: 
# 
# [32.0, 68.0, 86.0, 212.0]
#


def sumar(x, y):
    return x + y

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40]

resultado = list(map(sumar, lista1, lista2))

print(resultado)

# Resultado: 
# 
# [11, 22, 33, 44]
#


# usando funciones lambda que se verán con el tema  15-funciones
# numeros = [1, 2, 3, 4, 5, 6, 7, 38]
# cuadrados = map(lambda x: x**2, numeros)
# print(list(cuadrados))  # Salida: [1, 4, 9, 16, 25, 36, 49, 1444]
