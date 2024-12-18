def ejemplo_posicional(nombre, edad, /):
    print(f"nombre: {nombre}, edad: {edad}")

# Correcto
ejemplo_posicional("Alicia", 30)

# Incorrecto
# ejemplo_posicional(nombre="Alicia", edad=30)  
# TypeError: ejemplo_posicional() got some positional-only arguments passed as keyword arguments: 'nombre, edad'

def ejemplo_mixto(nombre, edad, /, a, b):
    print(f"nombre: {nombre}, edad: {edad}, A: {a}, B: {b}")


# Correcto
ejemplo_mixto("Alicia", 30, 10, 20)
ejemplo_mixto("Alicia", 30, a=10, b=20)

# Incorrecto
# ejemplo_mixto(nombre="Alicia", edad=30, a=10, b=20)  
# TypeError: ejemplo_mixto() got some positional-only arguments passed as keyword arguments: 'nombre, edad'

def ejemplo_nombre(*, key):
    print(f"Key: {key}")

# Correcto
ejemplo_nombre(key="valor")

# Incorrecto
# ejemplo_nombre("valor")  # TypeError: ejemplo_nombre() takes 0 positional arguments but 1 was given






