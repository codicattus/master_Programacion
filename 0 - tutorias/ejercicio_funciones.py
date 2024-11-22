def exponential(num: int, exp: int) -> int:
    resultado = num ** exp
    return resultado

   

numero = int(input("Introduce un número: "))
exponente = input("Introduce el exponente: ")


num_exp = int(exponente) if exponente else 2 # podríamos reasignar exponente = int(exponente) if exponente else 2 preo a MyPy no le gusta 
print(exponential(numero, num_exp))
print(exponential(numero, int(exponente) if exponente else 2)) # Esta opcion también es válida y quizá más "Pythonic", pero puede que resulte más dificil de comprender al principio.

