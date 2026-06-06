def fibo_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibo_recursive(n-1) + fibo_recursive(n-2)


print(fibo_recursive(7))
