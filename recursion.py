# Factorial in a non-recursive way

n = 7
fact = 1

while n > 0:
    fact *= n
    n -= 1

print(fact)
# -----------------------------------.

# Factorial in a recursive way


def factorial(nu):
    if nu < 1:
        return 1
    else:
        number = nu * factorial(nu-1)
        return number


print(factorial(7))

# ----------------------------------------

# fibonacci series


def fibonacci(num):
    a, b = 0, 1
    for x in range(num):
        a, b = b, a+b
    return a


print(fibonacci(4))


# fibonacci in a recursive way

