def generador():
    for i in range(5):
        yield i * 2

for indice, valor in enumerate(generador()):
    print(f"Índice: {indice}, Valor: {valor}")

# print(next(generador()))

