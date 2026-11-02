# 1. Count from 5 to 1 using recursion

def count(n):
    if n == 0:
        return

    print(n)
    count(n - 1)

count(5)


# 2. Factorial using recursion

def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)

print(fact(5))


# 3. Fibonacci series using recursion

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(5))