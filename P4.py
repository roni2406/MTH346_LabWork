def extended_euclid(a: int, b: int):
    if b == 0:
        # Base case
        return a, 1, 0
    gcd, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def modular_inverse(a: int, m: int):
    gcd, x, _ = extended_euclid(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for a = {a}, m = {m}")
    return x % m

# a)
a = 197654321
b = 1234567892
gcd, x, y = extended_euclid(a, b)
print(f"The answer for 4a: x = {x}, y = {y}, gcd = {gcd}")

# b)
a = 37
m = 2023
try:
    mod_inv = modular_inverse(a, m)
    print(f"The answer for 4b: The modular inverse of {a} mod {m} is {mod_inv}")
except ValueError as e:
    print(e)

# c)
a = 37 ** 2
m = 2023 ** 2
try:
    mod_inv = modular_inverse(a, m)
    print(f"The answer for 4c: The modular inverse of {a} mod {m} is {mod_inv}")
except ValueError as e:
    print(e)