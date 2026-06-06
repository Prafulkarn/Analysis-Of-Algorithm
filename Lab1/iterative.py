# Implementation and Complexity Analysis of Iterative, Numeric,and Recursive Algorithms in Python
# Ctrl+Alt+I for help
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for i in range(3, n+1):
        c = a+b
        a = b
        b = c
    return c


print(fibo(5))
