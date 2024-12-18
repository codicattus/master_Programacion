import os

# Obtener el directorio donde está el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, "Mitología griega.txt")

leer_archivo = open(ruta_archivo, "r", encoding="utf-8")
contenido = leer_archivo.read()
print(contenido)
leer_archivo.close()

