from helper import extended_euclid, modular_inverse

print("Question 4: ")
# a)
a = 197654321
b = 1234567892
gcd, x, y = extended_euclid(a, b)
print(f"4a: x = {x}, y = {y}, gcd = {gcd}")

# b)
a = 37
m = 2023
mod_inv = modular_inverse(a, m)
print(f"4b: The modular inverse of {a} mod {m} is {mod_inv}")

# c)
a = 37 ** 2
m = 2023 ** 2
mod_inv = modular_inverse(a, m)
print(f"4c: The modular inverse of {a} mod {m} is {mod_inv}\n")
