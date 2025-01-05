import math 

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

def tonelli_shanks(n, p):
    s = 0
    q = p - 1
    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1:
        r = modular_exponentiation(n, (p + 1) // 4, p)
        if (r * r) % p == n:
            return r
        return 0

    # Find the first quadratic non-residue z by brute-force search
    z = 1
    while modular_exponentiation(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = modular_exponentiation(z, q, p)
    r = modular_exponentiation(n, (q + 1) // 2, p)
    t = modular_exponentiation(n, q, p)
    m = s

    while t != 1:
        tt = t
        i = 0
        while tt != 1:
            tt = (tt * tt) % p
            i += 1
            if i == m:
                return 0

        b = modular_exponentiation(c, modular_exponentiation(2, m - i - 1, p - 1), p)
        b2 = (b * b) % p
        r = (r * b) % p
        t = (t * b2) % p
        c = b2
        m = i

    if (r * r) % p == n:
        return r
    return 0

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

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
    
def euclid_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a: int, b: int):
    if b == 0:
        # Base case
        return a, 1, 0
    if a < 0 or b < 0:
        gcd, x1, y1 = extended_euclid(abs(a), abs(b))
        if a < 0:
            x1 = -x1
        if b < 0:
            y1 = -y1
        return gcd, x1, y1
    gcd, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def modular_inverse(a: int, m: int):
    gcd, x, _ = extended_euclid(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for a = {a}, m = {m}")
    return x % m

def effective_fermat(p: int):
  if p % 4 != 1 and p != 2:
    return -1, -1
  ans = []
  for i in range(int(math.sqrt(p) + 1)):
    b_sq = p - i ** 2
    b = int(math.sqrt(b_sq))
    if b * b == b_sq:
      ans.append((i, b))
  return ans

def best_approx_rational(r: float, limit: int):
  terms = []
  for _ in range(limit):
    if r == 0:
      break
    r = 1/r
    a = int(r)
    terms.append(a)
    r -= a 
  
  num, denom = 1, 0
  for term in reversed(terms):
    num, denom = denom + term * num, num
  return denom, num, terms

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

# Jacobi symbol algorithm
def Jacobi(a, n):
    sigma = 1

    while True:
        a = a % n
        if a == 0:
            if n == 1:
                return sigma
            else:
                return 0            
        h = 0
        while a % 2 == 0:
            h += 1
            a //= 2
            
        # Quadratic reciprocity for powers of 2
        if h % 2 == 1 and n % 8 not in [1, 7]:
            sigma = -sigma
            
        # Quadratic reciprocity
        if a % 4 != 1 and n % 4 != 1:
            sigma = -sigma
            
        # Swap and continue
        a, n = n, a

def log_mod(base, value, modulus):
    x = 0
    while pow(base, x, modulus) != value and x < modulus:
        x += 1
    if x == modulus:
        raise ValueError("No solution exists")
    return x

def rdl(p, q, e, gamma, alpha):
    if e == 1:
        return log_mod(gamma, alpha, p)
    
    f = 1
    gamma_power_qe_minus_f = pow(gamma, pow(q, e-f), p)
    alpha_power_qe_minus_f = pow(alpha, pow(q, e-f), p)
    u = rdl(p, q, f, gamma_power_qe_minus_f, alpha_power_qe_minus_f)
    gamma_power_f = pow(gamma, pow(q, f), p)
    alpha_div_gamma_u = (alpha * pow(pow(gamma, u, p), p-2, p)) % p
    v = rdl(p, q, e-f, gamma_power_f, alpha_div_gamma_u)
    return pow(q, f) * v + u

def find_discrete_log(base, value, modulus):
    p = 2027
    q = 17
    e = 2
    return rdl(p, q, e, base, value)

def solving_congruence(a, b, n):
    d = euclid_algorithm(a, n)
    if b % d != 0:
        return "No solution"
    a //= d
    b //= d
    n //= d
    a_inv = modular_inverse(a, n)
    if b < 0:
        b = b % n
    return (a_inv * b) % n
 
def prime_factor(n):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

def compute_square_root(n, p):
    while (n >= p):
        n -= p
    return tonelli_shanks(n, p)

def compute_square_root_order_2(n, p):
    m = n
    while (n >= p):
        n -= p
    
    tmp = tonelli_shanks(n, p)
    a = 2*tmp*p

    while (m >= p*p):
        m -= p*p
    b = m - tmp*tmp

    # find h
    h = solving_congruence(a, b, p*p)
    return tmp + h*p