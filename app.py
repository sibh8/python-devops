def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)