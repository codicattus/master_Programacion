ciudades = ["Barcelona", "París", "Roma", "Londres", "Berlín"]
personajes = ["ratón", "Mickey", "pato", "Donald", "perro", "Pluto"]
numeros = [5, 7, 4, 2, 11, 25, 65, 1, 3, 4]
puntuacion = ["Mickey", 5, "Donald", 8, "Pluto", 9]

print(ciudades)
ciudades.sort()
print(ciudades)

# Resultado: 
# 
# ['Barcelona', 'París', 'Roma', 'Londres', 'Berlín']
# ['Barcelona', 'Berlín', 'Londres', 'París', 'Roma']

print(personajes)
personajes.sort()
print(personajes)
personajes.sort(key=str.lower)
print(personajes)

# Resultado: 
# 
# ['ratón', 'Mickey', 'pato', 'Donald', 'perro', 'Pluto']
# ['Donald', 'Mickey', 'Pluto', 'pato', 'perro', 'ratón']
# ['Donald', 'Mickey', 'pato', 'perro', 'Pluto', 'ratón']

print(numeros)
numeros.sort()
print(numeros)

# Resultado: 
# 
# [5, 7, 4, 2, 11, 25, 65, 1, 3, 4]
# [1, 2, 3, 4, 4, 5, 7, 11, 25, 65]

numeros.sort(reverse=True)
print(numeros)

# Resultado: 
# 
# [65, 25, 11, 7, 5, 4, 4, 3, 2, 1]

puntuacion.sort()
print(puntuacion)

# Resultado :
# TypeError: '<' not supported between instances of 'int' and 'str'
# Este error aparece a partir de la versión 3.
# En la versión 2 de Python permitía la comparación y ordenación de diferentes tipos, pero podía producir resultados no muy intuitivos.


# ********************************************************* #
# Igual que con el método reverse() existe la función reversed() que devuelve como resultado una lista ordenada al revés
# existe una función sorted() que devuelve una lista ordenada, sin modificar el original.