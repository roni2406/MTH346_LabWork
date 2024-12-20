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

def tonelli_shanks(n, p):
    # Tonelli-Shanks algorithm to find the square root of n modulo p.
    assert modular_exponentiation(n, (p - 1) // 2, p) == 1, "n is not a quadratic residue modulo p"

    if p % 4 == 3:
        return modular_exponentiation(n, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    z = 2
    while modular_exponentiation(z, (p - 1) // 2, p) != p - 1:
        z += 1

    m = s
    c = modular_exponentiation(z, q, p)
    t = modular_exponentiation(n, q, p)
    r = modular_exponentiation(n, (q + 1) // 2, p)

    while t != 1:
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = (t2i * t2i) % p
            if t2i == 1:
                break

        b = modular_exponentiation(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p

    return r

def find_sqrt_neg1_mod_p(p):
    """Find m such that m^2 + 1 = 0 (mod p)."""
    if p % 4 != 1:
        # For p = 3 (mod 4), m = (-1)^(p-1)/4 mod p
        exp = (p - 1) // 4
        m = modular_exponentiation(-1, exp, p)
        return m
    else:
        # For p = 1 (mod 4), use the Tonelli-Shanks algorithm
        return tonelli_shanks(p - 1, p)

# Given values of p
p_values = [2053, 3000017, 1234567913]

for p in p_values:
    try:
        m = find_sqrt_neg1_mod_p(p)
        print(f"For p = {p}, m such that m^2 + 1 \u2261 0 (mod p) is: {m}")
    except Exception as e:
        print(f"For p = {p}, an error occurred: {str(e)}")
