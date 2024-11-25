notas_alumnos = {
    "Javier": 8.7,
    "J. Luis": 7.3,
    "Arnau": 6.2,
    "Jana": 8.8,
    "Carla": 9.3
}

ciudades = {
    1 : "Barcelona",
    2 : "Madrid"
}

print(notas_alumnos)

# Resultado :
#
# {'Javier': 8.7, 'J. Luis': 7.3, 'Arnau': 6.2, 'Jana': 8.8, 'Carla': 9.3}

alumno_eliminado = notas_alumnos.pop("Arnau", "Alumno no encontrado")
print(f"Nota eliminada del alumno Arnau: {alumno_eliminado}")
print(notas_alumnos)
print(notas_alumnos.pop("Juan", "Alumno no encontrado"))

# Resultado : 
#
# Nota eliminada del alumno Arnau: 6.2
# {'Javier': 8.7, 'J. Luis': 7.3, 'Jana': 8.8, 'Carla': 9.3}
# Alumno no encontrado

alumno_eliminado = notas_alumnos.popitem()
print(f"Nota eliminada del alumno {alumno_eliminado[0]}: {alumno_eliminado[1]}")

# Resultado : 
#
# Nota eliminada del alumno Carla: 9.3

for _ in range(3):
    try:
        ciudad_eliminada = ciudades.popitem()
        print(f"Ciudad eliminada : {ciudad_eliminada[1]}")
    except:
        print("No quedan más registros a eliminar")

# Resultado : 
#
# Ciudad eliminada : Madrid
# Ciudad eliminada : Barcelona
# No quedan más registros a eliminar