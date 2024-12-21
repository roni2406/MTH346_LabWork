from helper import euler_totient, modular_exponentiation

print("Question 1: ")
# Part a: Find the last 3 digits of 2023^2024
n_a = 2023
exp_a = 2024
mod_a = 1000  # Last 3 digits means mod 1000
last_3_digits = modular_exponentiation(n_a, exp_a, mod_a)
print("1a: The last 3 digits of 2023^2024 are:", last_3_digits)

# Part b: Find the remainder when 20232024^20242023 is divided by 12345
n_b = 20232024
exp_b = 20242023
mod_b = 12345
phi_b = euler_totient(mod_b)
# Reduce the exponent mod 12345 using Euler's theorem
reduced_exp_b = exp_b % phi_b
remainder_b = modular_exponentiation(n_b, reduced_exp_b, mod_b)
print("1b: The remainder when 20232024^20242023 is divided by 12345 is:", remainder_b)

# Part c: Find the remainder when 19^(19^19) is divided by 1001
n_c = 19
mod_c = 1001
phi_c = euler_totient(mod_c)
# Compute 19^19 mod 1001
reduced_exp_c = modular_exponentiation(19, 19, phi_c)
remainder_c = modular_exponentiation(n_c, reduced_exp_c, mod_c)
print("1c: The remainder when 19^(19^19) is divided by 1001 is:", remainder_c, "\n")
