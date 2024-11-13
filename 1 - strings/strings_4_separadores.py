import time

name = "Miguel"
last_name = "Andrés"

print(name, last_name)
print(name, last_name, sep = None)
print(name, last_name, sep = " ")
print(name, last_name, sep = "")
print(name, last_name, sep = "     ")
print(name, last_name, sep = ",")
print(name, last_name, sep = "--")
print(name, last_name, sep = "\n")

# Resultado: 

# Miguel Andrés
# Miguel Andrés    
# Miguel Andrés    
# MiguelAndrés     
# Miguel     Andrés
# Miguel,Andrés    
# Miguel--Andrés   
# Miguel
# Andrés

print("Espera unos segundos", end=" ... ", flush=True)
time.sleep(3)
print("Listo! Gracias por la espera.")