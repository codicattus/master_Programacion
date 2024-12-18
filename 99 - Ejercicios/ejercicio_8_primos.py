# import time

def comprobar_numeros(dividendo):
    if dividendo <= 1:
        return False
    for divisor in range(2,dividendo):
        if dividendo % divisor == 0:
            break
    else:
        return True

# start_time = time.time()

numeros_primos = list(filter(comprobar_numeros, range(100)))

print(numeros_primos)

# end_time = time.time()
# print(f"Tiempo de ejecución: {end_time - start_time} segundos")


# Listado de números primos
# https://es.wikipedia.org/wiki/Anexo:N%C3%BAmeros_primos