def show_info(**kwargs: dict) -> None:
    """ Genera una cadena de información basada en argumentos clave-valor y la formatea de manera legible. 
    Este método toma cualquier cantidad de argumentos clave-valor (kwargs) y genera una cadena con la información, rodeada por líneas de asteriscos para mejorar la legibilidad. 
    :param kwargs: Argumentos clave-valor que representan la información a mostrar. 
    :type kwargs: dict 
    :return: Cadena formateada con la información proporcionada. 
    :rtype: str """
    
    info = f"\n{"*" * 30}\n"
    for clave, valor in kwargs.items():
        info = info + f"{clave}: {valor}\n"
    info = info + f"{"*" * 30}\n"
    return info

print(show_info(nombre="Juan", edad=18, ciudad="Barcelona"))
print(show_info(nombre="María", edad=20, ciudad="Madrid"))
print(show_info(nombre="Luis", ciudad="Madrid"))