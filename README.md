# Python Intermediate #9: Recursion

La recursión es un concepto en programación en el que una función se llama a sí misma para resolver un problema más pequeño. En Python, la recursión es una técnica útil para resolver problemas que pueden dividirse en subproblemas más simples. Aquí tienes un ejemplo de cómo funciona la recursión en Python:

Supongamos que queremos calcular el factorial de un número. El factorial de un número entero positivo n, denotado como n!, es el producto de todos los números enteros positivos menores o iguales a n. Por ejemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120.

Podemos calcular el factorial de un número utilizando una función recursiva de la siguiente manera:

```python
def factorial(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Calcular el factorial de 5
resultado = factorial(5)
print("El factorial de 5 es:", resultado)
```

Ahora, expliquemos cómo funciona este código:

1. Definimos una función `factorial` que toma un argumento `n`.
2. En la función `factorial`, primero verificamos si `n` es igual a 0. Si es así, devolvemos 1, ya que el factorial de 0 es 1. Este es nuestro caso base.
3. Si `n` no es igual a 0, entonces ejecutamos el caso recursivo. En el caso recursivo, calculamos `n * factorial(n - 1)`. Esto significa que calculamos el factorial de `n - 1` y lo multiplicamos por `n`.
4. Continuamos llamando a la función `factorial` con un argumento más pequeño en cada llamada hasta que alcanzamos el caso base.
5. Cuando alcanzamos el caso base, todas las llamadas recursivas se desenrollan y obtenemos el resultado final.

En este ejemplo, la recursión nos permite escribir un código más conciso y elegante para calcular el factorial de un número. Sin embargo, es importante tener cuidado al usar la recursión, ya que puede provocar un desbordamiento de pila si no se gestiona adecuadamente.

# Fibonacci

La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores. La secuencia comienza con 0 y 1, y luego cada número subsiguiente es la suma de los dos números anteriores. La secuencia de Fibonacci se ve así: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Aquí tienes un código de ejemplo en Python que genera los primeros n números de la secuencia de Fibonacci:

```python
def fibonacci(n):
    # Inicializamos los dos primeros números de la secuencia
    fib = [0, 1]
    # Generamos los siguientes números de la secuencia
    for i in range(2, n):
        # Sumamos los dos últimos números de la secuencia
        fib.append(fib[-1] + fib[-2])
    # Devolvemos la lista de los primeros n números de la secuencia
    return fib

# Solicitamos al usuario que ingrese la cantidad de números de Fibonacci que desea generar
n = int(input("Ingrese la cantidad de números de Fibonacci que desea generar: "))
# Generamos los primeros n números de la secuencia de Fibonacci
resultado = fibonacci(n)
# Imprimimos los resultados
print("Los primeros", n, "números de Fibonacci son:", resultado)
```

Ahora, expliquemos cómo funciona este código:

1. Definimos una función llamada `fibonacci` que toma un parámetro `n` que representa la cantidad de números de Fibonacci que queremos generar.
2. Inicializamos una lista `fib` con los dos primeros números de la secuencia de Fibonacci: 0 y 1.
3. Usamos un bucle `for` para generar los siguientes números de la secuencia. Comenzamos desde el tercer número (índice 2) hasta el número `n`.
4. En cada iteración del bucle, calculamos el siguiente número de Fibonacci sumando los dos últimos números de la lista `fib` y lo agregamos a la lista.
5. Finalmente, devolvemos la lista que contiene los primeros `n` números de la secuencia de Fibonacci.

Este código generará los primeros `n` números de la secuencia de Fibonacci y los imprimirá en la consola.