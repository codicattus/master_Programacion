def listar_serie_fibonacci(cantidad_numeros):
    f0 = 0
    f1 = 1
    if not cantidad_numeros:
        return 0
    sucesion_fibonacci=[f0, f1]
    while len(sucesion_fibonacci) < cantidad_numeros:
        fn = f0 + f1
        sucesion_fibonacci.append(fn)
        f0 = f1
        f1 = fn
    return sucesion_fibonacci
      

print(listar_serie_fibonacci(20))

# Serie de Fibonacci
# f0 = 0
# f1 = 1
# fn = fn-1 + fn-2
# https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci

# Refactorización del script anterior:


def serie_fibonacci(cantidad_numeros):
    f0, f1 = 0, 1
    if not cantidad_numeros:
        return 0
    sucesion_fibonacci=[f0, f1]
#    while len(sucesion_fibonacci) < cantidad_numeros:
    for _ in range(3,cantidad_numeros+1):
        sucesion_fibonacci.append(f0 + f1)
        f0, f1 = f1, f0 + f1
    return sucesion_fibonacci

print(serie_fibonacci(20))


def fibonacci_iter(n):
    if n <= 1:
        return n
    f0, f1 = 0, 1
    for _ in range(3, n + 1):
        f0, f1 = f1, f0 + f1
    return f1


n = 20
print(f"La posición número {n} de la serie Fibonacci es {fibonacci_iter(n)}")
