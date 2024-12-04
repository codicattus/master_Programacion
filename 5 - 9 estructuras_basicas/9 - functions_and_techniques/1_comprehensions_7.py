matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]
          ]

matriz_aplanada =[]
for fila in matriz:
    for elemento in fila:
        matriz_aplanada.append(elemento)

print(matriz_aplanada) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Aplanar la matriz (Método Phytonic)
aplanada = [elemento for fila in matriz for elemento in fila]
print(aplanada)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# O más Phytonic aún...
print([elemento for fila in matriz for elemento in fila])