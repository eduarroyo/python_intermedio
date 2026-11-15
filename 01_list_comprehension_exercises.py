from random import random

# 1. Genera una lista utilizando comprensión con los números del 0 al 10.
print([i for i in range(11)])

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.
squares = [i**2 for i in range(1, 11)]
print(squares)

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.
evens = [i for i in range(0, 21, 2)]
print(evens)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.
def to_farenheit(celsius:float):
    return (celsius*9/5)+32

celsius_list = [random()*100 for _ in range(10)]
farenheit_list = [to_farenheit(celsius) for celsius in celsius_list]
print(celsius_list, farenheit_list)

# 5. Crea una lista utilizando comprensión con los caracteres de una cadena.
print([ch for ch in "hola mundo!"])

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.
words = ["hola", "adios", "bye", "hasta luego"]
print([w for w in words if len(w)>4])

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.
def add5(number: float):
    return number+5

print([add5(n) for n in range(10,20)])

# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.
print([n>10 for n in range(8,14)])

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.
print([3*odd for odd in range(1,11) if odd%2==1])
print([n*3 if n%2!=0 else n for n in range(1,11)])

# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.
print([[n+(3*m) for n in range(1,4)] for m in range(0,3)])