num1 = 18
num2 = 3
num3 = 5
num4 = -7
num5 = "25"
num6 = 3+4j

print(f"Suma(+) :  {num1 + num2 = }")
print(f"Resta(-) :  {num1 - num2 = }")
print(f"Multiplicación(*) :  {num1 * num2 = }")
print(f"División(/) :  {num1 / num3 = }")
print(f"División con redondeo(//) :  {num1 // num3 = }")
print(f"Resto de una división(%) :  {num3 % num2 = }")
print(f"Negación(-) :  {-num3 = }")
print(f"Sin cambios(+) :  {+num4 = }")
print(f"Valor absoluto abs(num) :  {abs(num4) = }")
print(f"Valor absoluto abs(num) :  {abs(num4/num3) = }")
print(f"Convertir a entero int(num) :  {int(num5) = }")
print(f"Convertir a entero int(num) :  {int(int(num5) / num2) = }")
print(f"Convertir a float float(num) :  {float(num5) = }")
print(f"Convertir a float float(num) :  {float(num4) = }")
print(f"Convertir a número complejo complex(real, imag) :  {complex(num2, num4) = }")
print(f"Conjugado de un número complejo num.conjugate() :  {num6.conjugate() = }")
print(f"Devuelve en una tupla el resultado y el resto de una división divmod(numX, numY) :  {divmod(num3, num2) = }")
print(f"Devuelve el número elevado a la n potencia numX ** numY :  {num3 ** num2 = }")
print(f"Devuelve el número elevado a la n potencia pow(numX, numY) :  {pow(num3, num2) = }")
print(f"Con un tercer argumento, devuelve el resto de la operación pow(numX, numY, numZ) :  {pow(num3, num2, num3) = }")


# Resultado: 
#
# Suma(+) :  num1 + num2 = 21
# Resta(-) :  num1 - num2 = 15
# Multiplicación(*) :  num1 * num2 = 54
# División(/) :  num1 / num3 = 3.6
# División con redondeo(//) :  num1 // num3 = 3  
# Resto de una división(%) :  num3 % num2 = 2    
# Negación(-) :  -num3 = -5
# Sin cambios(+) :  +num4 = -7
# Valor absoluto abs(num) :  abs(num4) = 7       
# Valor absoluto abs(num) :  abs(num4/num3) = 1.4
# Convertir a entero int(num) :  int(num5) = 25  
# Convertir a entero int(num) :  int(int(num5) / num2) = 8
# Convertir a float float(num) :  float(num5) = 25.0
# Convertir a float float(num) :  float(num4) = -7.0
# Convertir a número complejo complex(real, imag) :  complex(num2, num4) = (3-7j)
# Conjugado de un número complejo num.conjugate() :  num6.conjugate() = (3-4j)
# Devuelve en una tupla el resultado y el resto de una división divmod(numX, numY) :  divmod(num3, num2) = (1, 2)
# Devuelve el número elevado a la n potencia numX ** numY :  num3 ** num2 = 125
# Devuelve el número elevado a la n potencia pow(numX, numY) :  pow(num3, num2) = 125
# Con un tercer argumento, devuelve el resto de la operación pow(numX, numY, numZ) :  pow(num3, num2, num3) = 0

