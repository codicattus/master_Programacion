nombre = "Miguel"

def saludar():
    print(f"Hola {nombre}")

def despedir(nombre):
    print(f"Adiós {nombre}")

def cambiar_nombre():
    nombre = "Vanessa"
    return nombre

# saludar("Juan")
# despedir("Lucas")
# print(cambiar_nombre())
# print(nombre)
nombre = cambiar_nombre()
print(nombre)
# saludar()