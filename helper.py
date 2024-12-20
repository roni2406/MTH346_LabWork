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

def euclid_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(A, M):
    m0 = M
    y = 0
    x = 1

    if (M == 1):
        return 0

    while (A > 1):
        # q is quotient
        q = A // M
        t = M
        # m is remainder now, process
        # same as Euclid's algo
        M = A % M
        A = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0):
        x = x + m0

    return x

def chinese_remainder(congruences):
  x = 0
  M = 1
  for _, mod in congruences:
    M *= mod
  
  for r, mod in congruences:
    m = M // mod 
    m_inverse = mod_inverse(m, mod)
    x += r * m * m_inverse

  return x % M