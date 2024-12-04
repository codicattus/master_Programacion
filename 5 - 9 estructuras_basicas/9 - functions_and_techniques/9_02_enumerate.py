# Añade un contador a un iterable.

frutas = ["manzana", "plátano", "pera", "fresa", "uva"]

# Usando enumerate para obtener el índice y el valor
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")

    
# Resultado: 
# 
# Índice 0: manzana
# Índice 1: plátano
# Índice 2: pera
# Índice 3: fresa
# Índice 4: uva