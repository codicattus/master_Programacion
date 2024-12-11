x = 10
if x > 0:
    print("x es positivo")

print("Esto se mostrará tanto si el número es positivo, negativo o 0")

# Resultado :
#
# x es positivo
# Esto se mostrará tanto si el número es positivo, negativo o 0
#

x = -4
if x > 0:
    print("x es positivo")
else:
    print("Esto solo se mostrará si el número no es positivo")

# Resultado :
#
# Esto solo se mostrará si el número no es positivo
#

x = 0
if x > 0:
    print("x es positivo")
elif x == 0:
    print("Esto solo se mostrará si el número es 0")
else:
    print("Esto solo se mostrará si el número no es positivo o 0")

# Resultado :
#
# Esto solo se mostrará si el número es 0
#


# En otros lenguajes de programación

# Javascript

"""
let numero = 5;

if (numero > 10) {
    console.log("El número es mayor que 10.");
} else if (numero > 5) {
    console.log("El número es mayor que 5 pero menor o igual a 10.");
} else {
    console.log("El número es menor o igual a 5.");
}
"""

# PHP

"""
$numero = 5;

if ($numero > 10) {
    echo "El número es mayor que 10.";
} elseif ($numero > 5) {
    echo "El número es mayor que 5 pero menor o igual a 10.";
} else {
    echo "El número es menor o igual a 5.";
}
"""

# Java

"""
public class Main 
{
    public static void main(String[] args) 
    {
        int numero = 5;

        if (numero > 10) {
            System.out.println("El número es mayor que 10.");
        } else if (numero > 5) {
            System.out.println("El número es mayor que 5 pero menor o igual a 10.");
        } else {
            System.out.println("El número es menor o igual a 5.");
        }
    }
}
"""

# C++

"""
#include <iostream>

int main() {
    int numero = 5;

    if (numero > 10) {
        std::cout << "El número es mayor que 10." << std::endl;
    } else if (numero > 5) {
        std::cout << "El número es mayor que 5 pero menor o igual a 10." << std::endl;
    } else {
        std::cout << "El número es menor o igual a 5." << std::endl;
    }

    return 0;
}
"""

# Rust

"""
fn main() {
    let numero = 5;

    if numero > 10 {
        println!("El número es mayor que 10.");
    } else if numero > 5 {
        println!("El número es mayor que 5 pero menor o igual a 10.");
    } else {
        println!("El número es menor o igual a 5.");
    }
}
"""