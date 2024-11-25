ciudades = ["Barcelona", "París", "Roma", "Londres", "Berlín"]

indice = ciudades.index("Roma")
print(indice)

# Resultado :
#
# 2

# indice = ciudades.index("Roma", 3)
# print(indice)

# Resultado :
#
# ValueError: 'Roma' is not in list

try:
    indice = ciudades.index("Roma", 3, 5) # Elemento a buscar, inicio de la búsqueda, fin de la busqueda.
except ValueError:
    print("Roma no se encuentra en la lista")
print(indice)

# Resultado :
#
# Roma no se encuentra en la lista