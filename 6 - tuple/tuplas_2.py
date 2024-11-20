ciudades = (
    "Barcelona", 1702814, 
    "París", 2206488, 
    "Roma", 2837332, 
    "Londres", 8982000, 
    "Berlín", 3645000, 
    "Sidney", 5312000, 
    "Nueva York", 8804000
    )

numeros = (1, 2, 3, 4, 5)


print(ciudades[4])

# Resultado :
#
# Roma

print(ciudades[:4])

# Resultado :
#
# ('Barcelona', 1702814, 'París', 2206488)

print(ciudades.count("Sidney"))

# Resultado :
#
# 1

print(ciudades.index("Sidney"))

# Resultado :
#
# 10

numeros += 6, 7, 8, 9

print(numeros)

# Resultado :
#
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
