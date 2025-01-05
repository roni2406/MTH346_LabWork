from helper import extended_euclid, modular_inverse

print("Question 3: ")
# a)
a = 1324567892
b = 187654321
gcd, x, y = extended_euclid(a, b)
print(f"4a: x = {x}, y = {y}, gcd = {gcd}")

# b)
a = 37
m = 2024
mod_inv = modular_inverse(a, m)
print(f"4b: The modular inverse of {a} mod {m} is {mod_inv}")

# c)
a = 37 ** 2
m = 2024 ** 2
mod_inv = modular_inverse(a, m)
print(f"4c: The modular inverse of {a} mod {m} is {mod_inv}\n")

a = -125
b = -275
gcd, x, y = extended_euclid(a, b)
print(f"4c: x = {x}, y = {y}, gcd = {gcd}")
