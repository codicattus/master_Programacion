# Combina varios iterables en un iterable de tuplas.

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinados = zip(lista1, lista2)
for num, letra in combinados:
    print(num, letra)  
    
# Resultado: 
# 
# (1, 'a'), (2, 'b'), (3, 'c')
#
