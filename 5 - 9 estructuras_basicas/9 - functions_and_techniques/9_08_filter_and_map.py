numeros = [1, 2, 3, 4, 5]

# Filtrar números pares y luego elevarlos al cuadrado
def square(num):
    return num ** 2

def is_even(num):
    return num % 2 == 0



resultado = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))
print(list(resultado))  # [4, 16]


