# Particularidades de las cadenas en Python

# --------------- INDEXACIÓN -------------- #

name = "Miguel"
print(name[0])
print(name[2])
print(name[::-1])
print(name[:2])
print(name[1:3])

# Resultado:
# M
# g
# l
# Mi
# ig
# ------------------------------------------#

# ------------- INMUTABILIDAD ------------- #

#name[0] = "T"
print(name)

# Resultado:
# TypeError: 'str' object does not support item assignment

# ------------------------------------------#

# ------------- ITERABILIDAD -------------- #

for letter in name:
    print(letter)

# Resultado:
# M
# i
# g
# u
# e
# l

# ------------------------------------------#
