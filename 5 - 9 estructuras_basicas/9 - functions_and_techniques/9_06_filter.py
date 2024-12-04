# Filtra elementos de un iterable que cumplen una condición.

def es_par(numero):
    return numero % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(es_par, numeros))

print(numeros_pares)  # Salida: [2, 4, 6, 8, 10]




# usando funciones lambda que se verán con el tema  15-funciones
# numeros = [1, 2, 3, 4, 5, 6, 7, 38]
# pares = filter(lambda x: x % 2 == 0, numeros)
# print(list(pares))  # Salida: [2, 4]
