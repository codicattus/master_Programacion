def tipo_objeto(objeto):
    if isinstance(objeto, (int, list)):
        print(f"{objeto} es un objeto de clase {type(objeto)}")
    elif isinstance(objeto, str):
        print(f"{objeto} es una cadena de texto")
    else:
        print(f"{objeto} no es ni una cadena de texto, ni un entero, ni una lista")

print(tipo_objeto("Sarandonga"))
print(tipo_objeto(5))
print(tipo_objeto(4.25))