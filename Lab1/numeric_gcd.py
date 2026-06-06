def gcd_algo(a: int, b: int):
    if a == 0 and b == 0:
        return "Undefined GCD"
    if b == 0:
        return a
    if a == 0:
        return b

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


print(gcd_algo(128, 42))
