from helper import extended_euclid, modular_inverse

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