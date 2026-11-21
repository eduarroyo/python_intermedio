### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
# def fizz_buzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)

# fizz_buzz()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
# def are_anagrams(word1:str, word2:str):
#     if word1 == word2 or len(word1) != len(word2):
#         return False

#     return sorted(word1) == sorted(word2)

# print(are_anagrams("hola", "hola"))
# print(are_anagrams("largo", "lar"))
# print(are_anagrams("largo", "abcde"))
# print(are_anagrams("palo", "lopa"))



"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
# def fibonacci(index: int):
#     if index < 0:
#         return None

#     if index == 0:
#         return [0]
#     if index == 1:
#         current = fibonacci(0)
#         current.append(1)
#         return current

#     current = fibonacci(index-1)
#     current.append(current[index-1]+current[index-2])
#     return current

# print(fibonacci(50))


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_prime(number: int):
    if number < 0:
        return False


    


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""