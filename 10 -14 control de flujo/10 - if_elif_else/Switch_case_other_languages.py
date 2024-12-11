# Javascript

"""
let dia = 3;
let mensaje;

switch (dia) {
    case 1:
        mensaje = "Lunes";
        break;
    case 2:
        mensaje = "Martes";
        break;
    case 3:
        mensaje = "Miércoles";
        break;
    default:
        mensaje = "Otro día";
}

console.log(mensaje);  // Miércoles
"""

# PHP

"""
$dia = 3;
$mensaje = "";

switch ($dia) {
    case 1:
        $mensaje = "Lunes";
        break;
    case 2:
        $mensaje = "Martes";
        break;
    case 3:
        $mensaje = "Miércoles";
        break;
    default:
        $mensaje = "Otro día";
}

echo $mensaje;  // Miércoles
"""

# Java

"""
public class Main {
    public static void main(String[] args) {
        int dia = 3;
        String mensaje;

        switch (dia) {
            case 1:
                mensaje = "Lunes";
                break;
            case 2:
                mensaje = "Martes";
                break;
            case 3:
                mensaje = "Miércoles";
                break;
            default:
                mensaje = "Otro día";
        }

        System.out.println(mensaje);  // Miércoles
    }
}
"""

# C++

"""
#include <iostream>

int main() {
    int dia = 3;
    std::string mensaje;

    switch (dia) {
        case 1:
            mensaje = "Lunes";
            break;
        case 2:
            mensaje = "Martes";
            break;
        case 3:
            mensaje = "Miércoles";
            break;
        default:
            mensaje = "Otro día";
    }

    std::cout << mensaje << std::endl;  // Miércoles
    return 0;
}
"""

# Rust

"""
fn main() {
    let dia = 3;
    let mensaje = match dia {
        1 => "Lunes",
        2 => "Martes",
        3 => "Miércoles",
        _ => "Otro día",
    };

    println!("{}", mensaje);  // Miércoles
}
"""

# Esto mismo en Python podríamos hacerlo así:

# Opción 1 (usando diccionarios)

dia = 3

def obtener_mensaje(dia):
    return {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles"
    }.get(dia, "Otro día")

mensaje = obtener_mensaje(dia)
print(mensaje)  # Miércoles

# Opción 2 (Usando if-elif-else)

dia = 3

if dia == 1:
    mensaje = "Lunes"
elif dia == 2:
    mensaje = "Martes"
elif dia == 3:
    mensaje = "Miércoles"
else:
    mensaje = "Otro día"

print(mensaje)  # Miércoles
