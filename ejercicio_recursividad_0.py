def suma(numeros, resultado = 0):
    for numero in numeros:
        if type(numero) is int:
            resultado = resultado + numero
        elif type(numero) is list:
            resultado = suma(numero, resultado)
        else:
            continue
    return resultado      

numeros = [20, 10, 50, "25", "tres", [10, 10], "cuatro", [1, "1"]]

print(suma(numeros))

# Nota: En Python, cuando se llamas a una función recursivamente, 
# el valor de la variable se pasa por valor y no por referencia. 
# Esto significa que cualquier modificación hecha a la variable 
# dentro de la llamada recursiva no afecta al valor de resultado en el nivel anterior.

# Para solucionar esto, necesitas acumular el resultado devuelto por las llamadas recursivas.
