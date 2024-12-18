import os

archivo = "Mitología griega.txt"
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, archivo)

with open(ruta_archivo, "r", encoding="utf-8") as file:
    contenido = file.readlines() # Lee todo el archivo de golpe y crea una lista con cada una de las líneas
    # No es necesario llamar a close()


print(contenido)


