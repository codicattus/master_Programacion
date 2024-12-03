ciudades : tuple[str | int, ...] = (
    "Barcelona", 1702814, 
    "París", 2206488, 
    "Roma", 2837332, 
    "Londres", 8982000, 
    "Berlín", 3645000, 
    "Sidney", 5312000, 
    "Nueva York", 8804000
    )

numeros : tuple[int, ...]= (1, 2, 3, 4, 5)


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
print(f"La {id(numeros)=}")
numeros += 6, 7, 8, 9
print(f"La {id(numeros)=}")
print(numeros)

# Resultado :
#
# (1, 2, 3, 4, 5, 6, 7, 8, 9)


letras = ( "a", "b", ["c", "cc"], "d" )
print(letras)
print(type(letras))
letras[2][0] = "cc"

print(letras)

# Resultado :
#
# ('a', 'b', ['c', 'cc'], 'd')
# <class 'tuple'>
# ('a', 'b', ['cc', 'cc'], 'd')