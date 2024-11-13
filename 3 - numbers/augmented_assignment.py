a = 5
b = 3

a += b  # Equivalente a: a = a(5) + b(3)
print(a)  

a -= b  # Equivalente a: a = a(8) - b(3)
print(a)  

b *= 2  # Equivalente a: b = b(3) * 2 
print(b)  

b /= 2  # Equivalente a: b = b(6) / 2 
print(b)  

a //= 2  # Equivalente a: a = a(5) // 2 
print(a)  

b %= 2  # Equivalente a: a = b(3) // 2 
print(b)  

a **= 3  # Equivalente a: a = a(2) ** 3 
print(a)  
 

print(f"En este momento el valor binario de a es {a}, que en binario es: {bin(a)}")
print(f"En este momento el valor binario de b es {b}, que en binario, después de convertirlo a integer, es: {bin(int(b))}")

b = int(b)
a &= b   # Equivalente a 8 (1000) & 1 (0001)
print(a)

a |= 5   # Equivale a 0 (0000) | 5 (0101)
print(a)

a ^= 2   # Equivale a 5 (0101) ^ 2 (0010)
print(a)

a <<= 2   # Equivale a 7 (0111) << 2  resultado en binario 11100
print(a)

a >>= 2   # Equivale a 28 (11100) >> 2  resultado en binario 111
print(a)

# Resultado: 
#
# 8
# 5
# 6
# 3.0
# 2
# 1.0
# 8
#
# En este momento el valor binario de a es 8, que en binario es: 0b1000
# En este momento el valor binario de b es 1.0, que en binario, después de convertirlo a integer, es: 0b1
#
# 0
# 5
# 7
# 28
# 7