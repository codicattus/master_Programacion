ciudades = ["Barcelona", "París", "Roma", "Londres", "Berlín"]

print(ciudades)
print(type(ciudades))

# Resultado :
# --------------------------------
# ['Barcelona', 'París', 'Roma', 'Londres', 'Berlín']
# <class 'list'>
# --------------------------------

ciudades.remove("Berlín")

print(ciudades)

# Resultado :
# --------------------------------
# ['Barcelona', 'París', 'Roma', 'Londres']
# --------------------------------

ciudad_eliminada = ciudades.pop()

print("-" * 20)
print(ciudad_eliminada)
print("-" * 20)

# Resultado :
# --------------------
# Londres
# --------------------

print(ciudades)

# Resultado :
# --------------------------------
# ['Barcelona', 'París', 'Roma']
# --------------------------------

ciudad_eliminada = ciudades.pop(1)

print("-" * 20)
print(ciudad_eliminada)
print("-" * 20)

# Resultado :
# --------------------
# París
# --------------------

print(ciudades)

# Resultado :
# --------------------------------
# ['Barcelona', 'Roma']
# --------------------------------

del ciudades[1]

print(ciudades)

# Resultado :
# --------------------------------
# ['Barcelona']
# --------------------------------

ciudades.clear()
print(ciudades)
print(type(ciudades))

# Resultado :
# --------------------------------
# []
# <class 'list'>
# --------------------------------