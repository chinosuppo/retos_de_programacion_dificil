### Reto #2: LA SUCESIÓN DE FIBONACCI ###

"""
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores. 0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    
    previo = 0
    siguiente = 1
    
    for index in range(0,50):
        print(previo)
        
        fibo = previo + siguiente
        previo = siguiente
        siguiente = fibo

fibonacci()