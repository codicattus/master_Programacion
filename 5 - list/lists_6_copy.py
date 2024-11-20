import copy

ciudades = ["Barcelona", "París", "Roma", "Londres", "Berlín"]


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
# La dirección de memoria de la lista ciudades es: 1452622270848
# La dirección de memoria de la lista cities es: 1452625394560  
# La dirección de memoria de la ciudades[0] es: 1452625313072   
# La dirección de memoria de la cities[0] es: 1452625313072  

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


numeros = [1, [21, 22, 23], 3, 4, [51, 52], 6, 7 , 8]

numbers = numeros.copy()

print("=========================")
print(id(numeros[1]))
print(id(numbers[1]))

# Resultado :
#
# [1, [21, 22, 23], 3, 4, [51, 52], 6, 7, 8]
# [1, [21, 22, 23], 3, 4, [51, 52], 6, 7, 8]
#

print("+++++++++++++++++++++++++++++++++++++++++++")
numbers.pop()

print("-------------------------------------------")
numbers[1].pop()

print("**********************************************")
print(numeros)
print(numbers)
print("**********************************************")

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
numeros[1].pop()

print(numeros)
print(numbers_deep_copy)

# Resultado :
#
# [1, [21, 22], 3, 4, [51, 52], 6, 7, 8]
# [1, [21, 22, 23], 3, 4, [51, 52], 6, 7, 8]
#