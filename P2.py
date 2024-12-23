from helper import find_sqrt_neg1_mod_p

# Given values of p
p_values = [2053, 3000017, 1234567913]
print("Question 2:")
for p in p_values:
    m = find_sqrt_neg1_mod_p(p)
    print(f"For p = {p}, m such that m^2 + 1 \u2261 0 (mod p) is: {m}")
print(" ")