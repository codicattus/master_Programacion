frutas = [(10, "manzanas"), (12, "peras"), (3, "sandías"), (14, "naranjas")]

for kilos, fruta in frutas:
    if fruta == "sandías":
        print(f"Cantidad: {kilos} {fruta}.")
        break
    else:
        print(f"Cantidad: {kilos}kg. de {fruta}.")

# Resultado
#
# Cantidad: 10kg. de manzanas.
# Cantidad: 12kg. de peras.
# Cantidad: 3 sandías.