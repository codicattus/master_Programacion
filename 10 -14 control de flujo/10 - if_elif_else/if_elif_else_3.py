# Operador ternario
# Expresión condicional ternaria
# "if-else" ternario
# "if expresion"

resultado = "verdadero" if 5>4 else "falso"
print(resultado)

# Resultado :
#
# verdadero
#

# El siguiente ejemplo es a modo de muestra ya que su uso puede estar
# desanconsejado por su posible falta de legibilidad

opcion_1 = 5
opcion_2 = 5
opcion_3 = 3

resultado = "izquierda" if opcion_1 > opcion_2 else "centro" if opcion_1 > opcion_3 else "derecha"
print(resultado)





a = 5
b = 3
c = 7

# Expresión booleana compuesta

if a >= b & b <= c:
    print(f"Se cumple la condición")
else:
    print("No se cumple la condición")    

if a >= b and b <= c:
    print(f"Se cumple la condición")
else:
    print("No se cumple la condición")    

# Comparación encadenada

if a >= b <= c:
    print(f"La variable a es mayor que b y b es menor que c")
else:
    print("No se cumple la condición")
