"""
Gestor de Inventario de una Tienda de Ropa

Crear un programa que gestione el inventario de una tienda de ropa donde:

1. Tendrás un inventario inicial con esta estructura:
   - Cada prenda será un diccionario con: nombre, precio, tallas disponibles y cantidad por talla
   - El inventario será una lista de estas prendas

2. El programa deberá:
   a) Mostrar todo el inventario de forma ordenada
   b) Buscar prendas por nombre (sin importar mayúsculas/minúsculas)
   c) Mostrar todas las prendas de un rango de precio específico
   d) Actualizar la cantidad de una prenda en una talla específica
   e) Mostrar las prendas con poco stock (menos de 3 unidades en alguna talla)

Datos de ejemplo para iniciar el inventario:
inventario = [
    {
        "nombre": "Camiseta Básica",
        "precio": 15.99,
        "tallas": {"S": 5, "M": 4, "L": 7}
    },
    {
        "nombre": "Pantalón Vaquero",
        "precio": 49.99,
        "tallas": {"M": 6, "L": 8, "XL": 2}
    },
    {
        "nombre": "Sudadera",
        "precio": 29.99,
        "tallas": {"S": 2, "M": 8, "L": 3}
    }
]
"""