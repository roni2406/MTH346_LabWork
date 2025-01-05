from helper import find_sqrt_neg1_mod_p, is_prime
import math



   
# Given values of p
p_values = [2029, 474993, 1003001]
print("Question 2:")
for p in p_values:
    if is_prime(p) == False:
        print(f"For p = {p}, m such that m^2 + 1 \u2261 0 (mod p) is: No solution")
    else: 
        m = find_sqrt_neg1_mod_p(p)
        print(f"For p = {p}, m such that m^2 + 1 \u2261 0 (mod p) is: {m}")
print(" ")