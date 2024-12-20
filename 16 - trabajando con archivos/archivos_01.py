from pathlib import Path

archivo = "Mitología griega.txt"
# Con solo el nombre del archivo es probable que algunos IDE nos de algún problema

print(archivo)
leer_archivo = open(archivo, "r", encoding="UTF-8")
contenido = leer_archivo.read()  # Lee TODO el contenido del archivo de golpe
print(contenido)
leer_archivo.close() # Es importante cerrar el archivo después de usarlo para liberar los recursos del sistema.


# archivo = Path("Mitología griega.txt")
# print(archivo.read_text())

