alumnos = ["Juan", "Alba", "Jesús", "Chris", "Lara"]
calificaciones = [6, 8, 9, 5, 6]
init_calificaciones = dict.fromkeys(alumnos, 0)

print(init_calificaciones)

# Resultado : 
#
# {'Juan': 0, 'Alba': 0, 'Jesús': 0, 'Chris': 0, 'Lara': 0}

init_calificaciones["Juan"] = 5
init_calificaciones["Alba"] = 6

print(init_calificaciones)

# Resultado : 
#
# {'Juan': 5, 'Alba': 6, 'Jesús': 0, 'Chris': 0, 'Lara': 0}


init_calificaciones = dict.fromkeys(alumnos, [])
print(init_calificaciones)

# Resultado : 
#
# {'Juan': [], 'Alba': [], 'Jesús': [], 'Chris': [], 'Lara': []}

init_calificaciones["Juan"].append(1)
print(init_calificaciones)

# Resultado : 
#
# {'Juan': [1], 'Alba': [1], 'Jesús': [1], 'Chris': [1], 'Lara': [1]}

calificaciones_alumno = dict(zip(alumnos, calificaciones))
print(calificaciones_alumno)

# Resultado : 
#
# {'Juan': 6, 'Alba': 8, 'Jesús': 9, 'Chris': 5, 'Lara': 6}