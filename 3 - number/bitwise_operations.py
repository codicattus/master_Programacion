a = 12  # binario: 1100
b = 10  # binario: 1010

resultado = a & b
print(f"{bin(resultado)}")  
print(f"{a & b = } -> {bin(resultado)}")
# Compara cada bit de dos números; el resultado es 1 si ambos bits son 1, de lo contrario, es 0.  

resultado = a | b
print(f"{bin(resultado)}")  
print(f"{a | b = } -> {bin(resultado)}")  
# Compara cada bit de dos números; el resultado es 1 si al menos uno de los bits es 1.  

resultado = a ^ b
print(f"{bin(resultado)}")  
print(f"{a ^ b = } -> {bin(resultado)}")  
# Compara cada bit de dos números; el resultado es 1 si solo uno de los bits es 1, de lo contrario, es 0. 
 
resultado = ~a
print(f"{bin(resultado)}")  
print(f"{~a = } -> {bin(resultado)}")  
# Invierte todos los bits de un número; cambia los bits 1 a 0 y viceversa. 

resultado = ~a
print(f"{bin(resultado)}")  
print(f"{~a = } -> {bin(resultado)}")  
# Desplaza los bits de un número a la izquierda y agrega ceros al final. Cada desplazamiento a la izquierda es equivalente a multiplicar por 2. 




# Resultado:
#
# a & b = 8 -> 0b1000
a = 12  # binario: 1100
b = 10  # binario: 1010

resultado = a & b
print(f"{bin(resultado)}")  
print(f"{a & b = } -> {bin(resultado)}")
# Compara cada bit de dos números; el resultado es 1 si ambos bits son 1, de lo contrario, es 0.  

resultado = a | b
print(f"{bin(resultado)}")  
print(f"{a | b = } -> {bin(resultado)}")  
# Compara cada bit de dos números; el resultado es 1 si al menos uno de los bits es 1.  

resultado = a ^ b
print(f"{bin(resultado)}")  
print(f"{a ^ b = } -> {bin(resultado)}")  
# Compara cada bit de dos números; el resultado es 1 si solo uno de los bits es 1, de lo contrario, es 0. 
 
resultado = ~a
print(f"{bin(resultado)}")  
print(f"{~a = } -> {bin(resultado)}")  
# Invierte todos los bits de un número; cambia los bits 1 a 0 y viceversa. 

resultado = a << 2
print(f"{bin(resultado)}")  
print(f"{a << 2 = } -> {bin(resultado)}")  
# Desplaza los bits de un número a la izquierda y agrega ceros al final. Cada desplazamiento a la izquierda es equivalente a multiplicar por 2. 

resultado = a >> 2
print(f"{bin(resultado)}")  
print(f"{a >> 2 = } -> {bin(resultado)}")  
# Desplaza los bits de un número a la derecha. Cada desplazamiento a la derecha es equivalente a dividir por 2. 



# Resultado:
#
# a & b = 8 -> 0b1000


