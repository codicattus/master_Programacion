def dividir():
    try:
        a = float(input("Introduce el dividendo: "))
        b = float(input("Introduce el divisor: "))
        resultado = a / b
    except ValueError:
        print("Error: El valor introducido no es un número.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"El resultado de la división es: {resultado}")
    finally:
        print("Finalizando la operación de división.")

# Llamar a la función
dividir()


