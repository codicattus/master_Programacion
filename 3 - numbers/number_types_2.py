from decimal import Decimal
from fractions import Fraction

num_1 = 0.1
num_2 = 0.2
print(f"{num_1} + {num_2} = {num_1 + num_2}")

num1 = Decimal(str(num_1))
num2 = Decimal(str(num_2))
suma = num1 + num2
print(f"{num1} + {num2} = {suma}")

# ----------------------------------------
# Resultado: 
#
# 0.1 + 0.2 = 0.30000000000000004
# 0.1 + 0.2 = 0.3
#
# ----------------------------------------

fract_1 = Fraction(4,3)
fract_2 = Fraction(5,3)

suma_fract = fract_1 + fract_2
mult_fract = fract_1 * fract_2
print(f"{fract_1 + fract_2 = }")
print(suma_fract)
print(mult_fract)

# ----------------------------------------
# Resultado: 
#
# fract_1 + fract_2 = Fraction(3, 1)
# 3
# 20/9
# ----------------------------------------