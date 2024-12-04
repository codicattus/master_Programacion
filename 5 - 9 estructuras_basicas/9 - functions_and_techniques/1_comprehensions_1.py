# Listas y Sets
# Permiten crear nuevas listas o conjuntos basados en los elementos de iterables existentes.

lista = [1, 2, 3, 4]
nueva_lista = [elemento * 2 for elemento in lista]
print(nueva_lista)

# O acortando aún más...
print([item * 3 for item in lista]) 

# Resultado:
# 
# [2, 4, 6, 8]
# [3, 6, 9, 12]
