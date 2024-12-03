# El operador walrus (:=) permite asignar un valor a una variable 
# y al mismo tiempo retornar ese valor dentro de una expresión.
# Su nombre oficial es operador de asignación de expresión.

# Sin operador walrus

nums = [1, 2, 3, 4, 5]
resultado = []
for num in nums:
    cuadrado = num ** 2
    resultado.append(cuadrado)
print(resultado)

# Con operador walrus

nums = [1, 2, 3, 4, 5]
resultado = []
for num in nums:
    resultado.append(cuadrado := num ** 2)
print(resultado)




