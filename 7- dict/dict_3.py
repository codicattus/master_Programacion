ciudades = {
    "Galicia" : ("Lugo", "Orense", "Pontevedra", "A Coruña"),
    "Andalucía" : ("Málaga", "Granada", "Huelva", "Jaén", "Sevilla", "Córdoba", "Cádiz", "Almería"),
    "Euskadi" : ("Álava", "Guipúzcoa", "Vizcaya")
}

notas_alumnos = {
    "Javier": 8.7,
    "J. Luis": 7.3,
    "Arnau": 6.2,
    "Jana": 8.8,
    "Carla": 9.3
}

"""Los métodos keys() y values() de un diccionario en Python devuelven vistas que contienen todas las claves o todos los valores del diccionario, respectivamente. 
Estas vistas no permiten el acceso directo a un único elemento por su índice. Sin embargo, se puede convertir estas vistas a listas para acceder a elementos específicos por índice."""

print(notas_alumnos.keys()) 
print(notas_alumnos.values())

# Resultado :
# 
# dict_keys(['Javier', 'J. Luis', 'Arnau', 'Jana', 'Carla'])
# dict_values([8.7, 7.3, 6.2, 8.8, 9.3])
#

alumnos = list(notas_alumnos.keys())
calificaciones = list(notas_alumnos.values())

print(alumnos)
print(alumnos[0])
print(calificaciones[0])

# Resultado :
#
# ['Javier', 'J. Luis', 'Arnau', 'Jana', 'Carla']
# Javier
# 8.7
