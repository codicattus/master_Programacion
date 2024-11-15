ciudades = ["Barcelona", "París", "Roma", "Londres", "Berlín"]
print(ciudades[0])
print(ciudades[2])
print(ciudades[-1])

# Resultado:
# ---------------------------
# Barcelona
# Roma
# Berlín
# ---------------------------

ciudades[2] = "Milán"
print(ciudades[2])

# Resultado:
# ---------------------------
# Milán
# ---------------------------

ciudades.append(["Brasilia", "Río de Janeiro"])
print(ciudades[5])

# Resultado:
# ---------------------------
# ['Brasilia', 'Río de Janeiro']
# ---------------------------

ciudades.extend(["Montevideo", "Buenos Aires"])
print(ciudades[6])
print(ciudades[7])

# Resultado:
# ---------------------------
# Montevideo
# Buenos Aires
# ---------------------------

ciudades.insert(0, "Kiev")
print(ciudades[0])
print(ciudades[1])

# Resultado:
# ---------------------------
# Kiev
# Barcelona
# ---------------------------
