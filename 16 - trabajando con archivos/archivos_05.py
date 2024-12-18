import os

archivo = "La Revolución Industrial.txt"
directorio_actual = os.path.dirname(os.path.abspath(__file__))


ruta_archivo = os.path.join(directorio_actual, os.pardir, "recursos", "archivos", archivo)
ruta_archivo = os.path.abspath(ruta_archivo)


with open(ruta_archivo, "r", encoding="UTF-8") as file:
    for line in file: # Carga líne a línea
        print(line)