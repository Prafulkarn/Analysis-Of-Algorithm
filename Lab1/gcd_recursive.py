def gcd_recursive(a, b):
    if a == 0 and b == 0:
        return "Undefined GCD"
    if a == 0:
        return b
    if b == 0:
        return a

    return gcd_recursive(b, a % b)


print(gcd_recursive(128, 42))
