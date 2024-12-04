def abrir_archivo(nombre_archivo):
    if not nombre_archivo.endswith('.txt'):
        raise ValueError("Solo se permiten archivos .txt")
    # Suponemos que el archivo se abre y se devuelve el contenido
    return "contenido del archivo"

def procesar_contenido(contenido):
    if not contenido:
        raise ValueError("El contenido está vacío")
    # Lógica para procesar el contenido
    print("Procesando:", contenido)

def main():
    while True:
        try:
            nombre_archivo = input("Introduce el nombre del archivo (terminado en .txt): ")
            contenido = abrir_archivo(nombre_archivo)
            procesar_contenido(contenido)
            break  # Salir del bucle si todo está bien
        except ValueError as e:
            print(f"Error: {e}")
            print("Por favor, inténtalo de nuevo.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            break  # Salir del bucle en caso de errores inesperados

main()
