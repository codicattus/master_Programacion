# Listas y Sets
# Permiten crear nuevas listas o conjuntos basados en los elementos de iterables existentes.

lista = [1, 2, 3, 4]
nueva_lista = [x * 2 for x in lista]
print(nueva_lista)

print([x * 3 for x in lista]) 

# Resultado:
# 
# [2, 4, 6, 8]
# [3, 6, 9, 12]
