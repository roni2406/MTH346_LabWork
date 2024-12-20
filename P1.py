# Helper functions for modular arithmetic
from math import gcd

def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Part a: Find the last 3 digits of 2023^2024
n_a = 2023
exp_a = 2024
mod_a = 1000  # Last 3 digits means mod 1000
last_3_digits = modular_exponentiation(n_a, exp_a, mod_a)
print("The last 3 digits of 2023^2024 are:", last_3_digits)

# Part b: Find the remainder when 20232024^20242023 is divided by 12345
n_b = 20232024
exp_b = 20242023
mod_b = 12345
phi_b = euler_totient(mod_b)
# Reduce the exponent mod 12345 using Euler's theorem
reduced_exp_b = exp_b % phi_b
remainder_b = modular_exponentiation(n_b, reduced_exp_b, mod_b)
print("The remainder when 20232024^20242023 is divided by 12345 is:", remainder_b)

# Part c: Find the remainder when 19^(19^19) is divided by 1001
n_c = 19
mod_c = 1001
phi_c = euler_totient(mod_c)
# Compute 19^19 mod 1001
reduced_exp_c = modular_exponentiation(19, 19, phi_c)
remainder_c = modular_exponentiation(n_c, reduced_exp_c, mod_c)
print("The remainder when 19^(19^19) is divided by 1001 is:", remainder_c)
