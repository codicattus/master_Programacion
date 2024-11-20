print("******************************************************************")

a = 10
b = a

print("******************************************************************")

print(f"El puntero de a apunta a {id(a)}")
print(f"El puntero de b apunta a {id(b)}")

# Resultado :
#
# El puntero de a apunta a 140723210353368
# El puntero de b apunta a 140723210353368
#

b = 15

print(f"El puntero de b apunta a {id(b)}")

# Resultado :
#
# El puntero de b apunta a 140723210353528
#

c = 15

print(f"El puntero de b apunta a {id(c)}")

# Resultado :
#
# El puntero de c apunta a 140723210353528
#

if c == b :
    print(f"La variable {b=} y la variable {c=} son iguales.")
else:
    print(f"La variable {b=} y la variable {c=} son distintas.")

# Resultado :
#
# La variable b=15 y la variable c=15 son iguales.
#

if c is b :
    print(f"La variable {b=} y la variable {c=} son iguales.")
else:
    print(f"La variable {b=} y la variable {c=} son distintas.")

# Resultado :
#
# La variable b=15 y la variable c=15 son iguales.
#

print("********************************************************************")

aa = []
bb = []

print("******************************************************************")

print(f"El puntero de aa apunta a {id(aa)}")
print(f"El puntero de bb apunta a {id(bb)}")

# Resultado :
#
# El puntero de aa apunta a 2408829278464
# El puntero de bb apunta a 2408829276544
#

if aa == bb :
    print(f"La variable {aa=} y la variable {bb=} son iguales.")
else:
    print(f"La variable {aa=} y la variable {bb=} son distintas.")

# Resultado :
#
# La variable aa=[] y la variable bb=[] son iguales.
#

if aa is bb :
    print(f"La variable {aa=} y la variable {bb=} son iguales.")
else:
    print(f"La variable {aa=} y la variable {bb=} son distintas.")

# Resultado :
#
# La variable aa=[] y la variable bb=[] son distintas.
#

aa.append(5)
bb.append(5)

print(f"{aa=}")
print(f"{bb=}")

if aa == bb :
    print(f"La variable {aa=} y la variable {bb=} son iguales.")
else:
    print(f"La variable {aa=} y la variable {bb=} son distintas.")

# Resultado :
#
# aa=[5]
# bb=[5]
# La variable aa=[5] y la variable bb=[5] son iguales.
#

if aa is bb :
    print(f"La referencia a la variable {aa=} y la referencia variable {bb=} son iguales.")
else:
    print(f"La referencia variable {aa=} y la referencia variable {bb=} son distintas.")

# Resultado :
#
# La referencia variable aa=[5] y la referencia variable bb=[5] son distintas.
#

if aa[0] is bb[0] :
    print(f"La referencia a la variable {aa[0]=} {id(aa[0])} y la referencia variable {bb[0]=} {id(bb[0])} son iguales.")
else:
    print(f"La referencia variable {aa[0]=} {id(aa[0])} y la referencia variable {bb[0]=} {id(bb[0])}son distintas.")

# Resultado :
#
# La referencia a la variable aa[0]=5 140723210353208 y la referencia variable bb[0]=5 140723210353208 son iguales.
#

print("******************************************************************")

cc = []
dd = cc 

print("******************************************************************")

print(f"El puntero de cc apunta a {id(cc)}")
print(f"El puntero de dd apunta a {id(dd)}")

# Resultado :
#
# El puntero de cc apunta a 2447997337024
# El puntero de dd apunta a 2447997337024
#

if cc == dd :
    print(f"La variable {cc=} y la variable {dd=} son iguales.")
else:
    print(f"La variable {cc=} y la variable {dd=} son distintas.")

# Resultado :
#
# La variable b=15 y la variable c=15 son iguales.
#

if cc is dd :
    print(f"La variable {cc=} y la variable {dd=} son iguales.")
else:
    print(f"La variable {cc=} y la variable {dd=} son distintas.")

# Resultado :
#
# La variable b=15 y la variable c=15 son iguales.
#

print("*********************************************************")

cc.append(5)

print(cc)
print(dd)

# Resultado :
#
# [5]
# [5]
#

dd[0] = 10

print(cc)
print(dd)

# Resultado :
#
# [10]
# [10]
#