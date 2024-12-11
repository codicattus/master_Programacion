# Combina varios iterables en un iterable de tuplas.
# Devuelve un iterador de tuplas, no una lista de tuplas.#
# Esto significa que no se puede usar índices directamente 
# sobre el objeto retornado por zip sin convertirlo primero a una lista.

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinados = list(zip(lista1, lista2))

for num, letra in combinados:
    print(num, letra)  
    
# Resultado: 
# 
# (1, 'a'), (2, 'b'), (3, 'c')
#
