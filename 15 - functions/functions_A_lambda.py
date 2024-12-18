# Definiendo una función lambda para duplicar un número
duplicar = lambda x: x ** 2

# Usando la función lambda

print(duplicar(6))


sumar = lambda x, y: x + y

resultado = sumar(3, 5)
print(resultado)


notas_trimestre = [(3, 4, 8), (4, 5, 5), (5, 6, 6)]
lista_ordenada = sorted(
    notas_trimestre, 
    key=lambda x: (x[0] + x[1] + x[2]) / 3, 
    reverse=True
)
print(lista_ordenada)
