import os

archivo = "Mitología griega.txt"
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, archivo)

with open(ruta_archivo, "r", encoding="utf-8") as file:
    for line in file: # Carga líne a línea
        print(line)
