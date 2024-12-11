def generador():
    for i in range(5):
        yield i * 2

#for indice, valor in enumerate(generador()):
 #   print(f"Índice: {indice}, Valor: {valor}")

nuevo_valor = generador()
input("introduce un valor: ")
print(next(nuevo_valor))
input("introduce un valor: ")
print(next(nuevo_valor))
input("introduce un valor: ")
print(next(nuevo_valor))


