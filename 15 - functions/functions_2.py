def funct_default_parameters(nom_user: str = "usuario", email: str = "email@dominio.com") -> None:
    print(f"Hola, {nom_user}. Correo electrónico: {email}")


funct_default_parameters("Miguel", "codicattus@gmail.com")
funct_default_parameters()

# Resultado :
#
# Hola, Miguel. Correo electrónico: codicattus@gmail.com
# Hola, usuario. Correo electrónico: email@dominio.com
#

funct_default_parameters(email="codicattus@gmail.com")

# Resultado :
#
# Hola, usuario. Correo electrónico: codicattus@gmail.com
#

def mult_5(num1: int, num2: int=5) -> int:
    return num1 * num2

print(mult_5(8))
print(mult_5(8, 4))

# Resultado :
#
# 40
# 32
#




