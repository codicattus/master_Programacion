count = 0
while count < 5:
    print(count)
    count += 1

# Resultado :
#
# 0
# 1
# 2
# 3
# 4


# Opciones otros lenguajes

# javascript

"""
let i = 0;

// Bucle while
while (i < 5)
{
    console.log(i); 
    i++;
}

i = 0;

// Bucle do-while
do 
{
    console.log(i);
    i++;
} while (i < 5);
"""

# PHP

"""
$i = 0;

// Bucle while
while ($i < 5) 
{
    echo $i . "\n";
    $i++;
}

$i = 0;

// Bucle do-while
do 
{
    echo $i . "\n";
    $i++;
} while ($i < 5);

"""

# Java

"""
public class Main 
{
    public static void main(String[] args) 
    {
        int i = 0;

        // Bucle while
        while (i < 5) 
        {
            System.out.println(i);
            i++;
        }

        i = 0;

        // Bucle do-while
        do 
        {
            System.out.println(i);
            i++;
        } while (i < 5);
    }
}
"""

# C++

"""
#include <iostream>

int main() 
{
    int i = 0;

    // Bucle while
    while (i < 5) 
    {
        std::cout << i << std::endl;
        i++;
    }

    i = 0;

    // Bucle do-while
    do 
    {
        std::cout << i << std::endl;
        i++;
    } while (i < 5);

    return 0;
}
"""

# Rust

"""
fn main() 
{
    let mut i = 0;

    // Bucle while
    while i < 5 
    {
        println!("{}", i);
        i += 1;
    }

    i = 0;

    // Simular un bucle do-while
    loop 
    {
        println!("{}", i);
        i += 1;
        if i >= 5 
        {
            break;
        }
    }
}
"""