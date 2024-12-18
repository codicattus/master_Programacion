def leer_por_partes(archivo, tamano_buffer=512):
    with open(archivo, "r", encoding="utf-8") as file:
        while True:
            parte = file.read(tamano_buffer)
            if not parte:
                break
            yield parte



generador = leer_por_partes("14 - trabajando con archivos\El tesoro perdido de la selva.txt")
continuar = True

while continuar:
    try:
        print(next(generador))  # Muestra la siguiente parte del texto
        continuar = input("¿Quieres leer más? (s/n): ").strip().lower() == 's'
    except StopIteration:
        print("Fin del archivo.")
        continuar = False










""" def leer_por_partes(archivo, tamano_buffer=1024):
    with open(archivo, "r", encoding="utf-8") as file:
        buffer = ""
        while True:
            fragmento = file.read(tamano_buffer)
            if not fragmento:
                if buffer:
                    yield buffer
                break
            buffer += fragmento
            while " " in buffer:
                # Encuentra la última palabra completa en el buffer
                ultimo_espacio = buffer.rfind(" ")
                if ultimo_espacio == -1:
                    break
                # Devuelve el texto hasta el último espacio (palabra completa)
                yield buffer[:ultimo_espacio]
                # Guarda el resto del buffer para el siguiente ciclo
                buffer = buffer[ultimo_espacio + 1:] """