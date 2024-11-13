num1 = 15
num2 = -4.5
num3 = 5.3657
x = 3
y = 3


# Uso de métodos
print(num1.bit_length())  # Devuelve el número de bits necesarios para representar un número entero en binario, sin contar el signo.
print(num1.to_bytes(2, byteorder='big'))  # Convierte un entero en una secuencia de bytes.

# Resultado :
#
# 4
# b'\x00\x0f'


# Uso de funciones
print(abs(num2))  # Devuelve el valor absoluto de un número.
print(round(num3, 1))  # Redondea un número a n dígitos decimales.
print(pow(x, y, 2))  # Devuelve x elevado a la potencia 𝑦, y si se proporciona, el resto de dividir el resultado por el tercer parámetro.
print(divmod(9, 4))  # Devuelve una tupla que contiene el cociente y el residuo (resto) de dividir x por y.
print(sum([1, 2, 3, 4]))  # Devuelve la suma de una secuencia de números.
print(max(3, 7, 2))  # Devuelve el elemento más grande de una secuencia o entre varios argumentos.
print(min(3, 7, 2))  # Devuelve el elemento más pequeño de una secuencia o entre varios argumentos.

# Resultado :
#
# 4.5
# 5.4 
# 27
# (2, 1)
# 10
# 7
# 2