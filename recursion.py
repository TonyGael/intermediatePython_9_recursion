# Factorial in a non recursive way

n = 7
fact = 1

while n > 0:
    fact *= n
    n -= 1

print(fact)
# -----------------------------------.

# Factorial in a recursive way
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))
