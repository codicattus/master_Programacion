import copy

ciudades = ["Barcelona", "París", "Roma", "Londres", "Berlín"]
numeros = [1, [21, 22, 23], 3, 4, [51, 52], 6, 7 , 8]

cities = ciudades.copy() # Hace una copia poco profunda (Shallow Copy)

print(ciudades)
print(cities)

print(f"La dirección de memoria de la lista ciudades es: {id(ciudades)}")
print(f"La dirección de memoria de la lista cities es: {id(cities)}")

print(f"La dirección de memoria de la ciudades[0] es: {id(ciudades[0])}")
print(f"La dirección de memoria de la cities[0] es: {id(cities[0])}")



# Resultado :
#
# ['Barcelona', 'París', 'Roma', 'Londres', 'Berlín']
# ['Barcelona', 'París', 'Roma', 'Londres', 'Berlín']
#

cities[0] = "Tokio"

print(ciudades)
print(cities)

print(f"La dirección de memoria de la lista ciudades es: {id(ciudades)}")
print(f"La dirección de memoria de la lista cities es: {id(cities)}")

print(f"La dirección de memoria de la ciudades[0] es: {id(ciudades[0])}")
print(f"La dirección de memoria de la cities[0] es: {id(cities[0])}")

# Resultado :
#
# ['Barcelona', 'París', 'Roma', 'Londres', 'Berlín']
# ['Tokio', 'París', 'Roma', 'Londres', 'Berlín']
#

numbers = numeros.copy()

print(numeros)
print(numbers)

# Resultado :
#
# [1, [21, 22, 23], 3, 4, [51, 52], 6, 7, 8]
# [1, [21, 22, 23], 3, 4, [51, 52], 6, 7, 8]
#

numbers[1].pop()

print(numeros)
print(numbers)

# Resultado :
#
# [1, [21, 22], 3, 4, [51, 52], 6, 7, 8]
# [1, [21, 22], 3, 4, [51, 52], 6, 7, 8]
#

numbers_deep_copy = copy.deepcopy(numeros) # Hace una copia profunda (Deep Copy)

print(numeros)
print(numbers_deep_copy)

# Resultado :
#
# [1, [21, 22], 3, 4, [51, 52], 6, 7, 8]
# [1, [21, 22], 3, 4, [51, 52], 6, 7, 8]
#

numbers_deep_copy[1].append(23)

print(numeros)
print(numbers_deep_copy)

# Resultado :
#
# [1, [21, 22], 3, 4, [51, 52], 6, 7, 8]
# [1, [21, 22, 23], 3, 4, [51, 52], 6, 7, 8]
#