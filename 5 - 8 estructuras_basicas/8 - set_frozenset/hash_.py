texto = "Hola"
print(hash(texto))

conjunto = {5, "hola", (1, 2, 3), 1567}
for elemento in conjunto:
    print(f"El hash del elemento {elemento} es: {hash(elemento)}")

for _ in range(10):
    print(hash(texto))

# Un hash es un valor generado por una función hash, que toma una entrada y produce un número entero único que representa esa entrada. Este valor se utiliza para indexar datos en estructuras como diccionarios (dict) y conjuntos (set), permitiendo un acceso rápido y eficiente a los elementos. En resumen, un hash actúa como una especie de "huella digital" para datos, garantizando que cada elemento tiene un identificador único basado en su contenido.

# Desde Python 3.3, Python introduce una semilla aleatoria para la función de hash cada vez que se ejecuta el intérprete. Esto es una medida de seguridad para proteger contra ciertos tipos de ataques, conocidos como hash collision attacks. Como resultado, los valores de hash para el mismo objeto pueden cambiar entre ejecuciones del programa.

# Para obtener valores hash consistentes entre ejecuciones (por ejemplo, para fines de almacenamiento o comparación persistente), se puede usar el módulo hashlib que proporciona funciones de hash criptográficas. Estos valores no cambian entre ejecuciones.