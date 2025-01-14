from pathlib import Path

ruta_carpeta = Path(__file__).parent
ruta_archivo = ruta_carpeta / "Mitología griega.txt"

leer_archivo = open(ruta_archivo, "r", encoding="UTF-8")
contenido = leer_archivo.read()
print(contenido)
leer_archivo.close()

