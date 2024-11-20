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

poblaciones = ciudades.copy()
print(poblaciones)
print("-"* 30)
poblaciones.pop("Andalucía")
print(poblaciones)
print(ciudades)

print(notas_alumnos)
notas = notas_alumnos.items()

# Resultado : 
# {'Javier': 8.7, 'J. Luis': 7.3, 'Arnau': 6.2, 'Jana': 8.8, 'Carla': 9.3}

print("=============================================")
print("=============================================")

for nombre in notas_alumnos: 
    print(f"{nombre}: {notas_alumnos[nombre]}")

print("=============================================")
print("=============================================")

for nombre, calificacion in notas: 
    print(f"{nombre}: {calificacion}")

# Resultado : 
# =============================================
# =============================================
# Javier: 8.7
# J. Luis: 7.3
# Arnau: 6.2
# Jana: 8.8
# Carla: 9.3
# =============================================
# =============================================
# Javier: 8.7
# J. Luis: 7.3
# Arnau: 6.2
# Jana: 8.8
# Carla: 9.3

print("=============================================")
print(" == Modificamos un valor del diccionario  == ")
print("=============================================")

notas_alumnos["Javier"] = 5

print( " ======================================= ")

for nombre in notas_alumnos: 
    print(f"{nombre}: {notas_alumnos[nombre]}")

print("=============================================")
print("=============================================")

for nombre, calificacion in notas: 
    print(f"{nombre}: {calificacion}")

# Resultado :
#
# =============================================
#  == Modificamos un valor del diccionario  ==
# =============================================
#  =======================================
# Javier: 5
# J. Luis: 7.3
# Arnau: 6.2
# Jana: 8.8
# Carla: 9.3
# =============================================
# =============================================
# Javier: 5
# J. Luis: 7.3
# Arnau: 6.2
# Jana: 8.8
# Carla: 9.3