number_list = [1, 2, 3, 4, 17, 21, 33, 45]
for number in number_list:
    print(number)

# Resultado:
#
# 1
# 2
# 3
# 4
# 17
# 21
# 33
# 45

for number in number_list:
    if number % 2 == 0:
        print(f"El número {number} es par")

# Resultado :
#
# El número 2 es par
# El número 4 es par
# 

for char in "Hello":
    print(char)

# Resultado:
#
# H
# e
# l
# l
# o
#


# ejercicio_6.py









# En otros lenguajes de programación

# Javascript

""" 
let numeros = [1, 2, 3, 4, 5];

// Bucle for clásico
for (let i = 0; i < numeros.length; i++) 
{
    console.log(numeros[i]);
}

// Bucle for...of
for (let numero of numeros) 
{
    console.log(numero);
}

// Bucle for...in
for (let indice in numeros) 
{
    console.log(numeros[indice]);
}
 """

# PHP

"""
$numeros = array(1, 2, 3, 4, 5);


// Bucle for clásico
for ($i = 0; $i < count($numeros); $i++) 
{
    echo $numeros[$i] . "\n";
}

// Bucle foreach
foreach ($numeros as $numero) 
{
    echo $numero . "\n";
}
"""

# Java

"""
public class Main 
{
    public static void main(String[] args) 
    {
        int[] numeros = {1, 2, 3, 4, 5};

        // Bucle for clásico
        for (int i = 0; i < numeros.length; i++) 
        {
            System.out.println(numeros[i]);
        }

        // Bucle enhanced for (foreach)
        for (int numero : numeros) 
        {
            System.out.println(numero);
        }
    }
}
"""

# C++

"""
#include <iostream>

int main() 
{
    int numeros[] = {1, 2, 3, 4, 5};

    // Bucle for clásico
    for (int i = 0; i < sizeof(numeros)/sizeof(numeros[0]); i++) 
    {
        std::cout << numeros[i] << std::endl;
    }

    // Bucle range-based for (disponible desde C++11)
    for (int numero : numeros) 
    {
        std::cout << numero << std::endl;
    }

    return 0;
}
"""

# Rust

"""
fn main() {
    let numeros = [1, 2, 3, 4, 5];

    // Bucle for clásico en Rust
    for numero in numeros.iter() 
    {
        println!("{}", numero);
    }

    // Bucle con índice
    for (i, numero) in numeros.iter().enumerate() 
    {
        println!("Índice: {}, Valor: {}", i, numero);
    }
}
"""