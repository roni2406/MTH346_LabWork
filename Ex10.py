from helper import modular_inverse, euclid_algorithm, chinese_remainder
def pow_mod(x, n, p):
    if n == 0:
        return 1
    if n % 2 == 1:
        return (pow_mod(x, n - 1, p) * x) % p
    x = pow_mod(x, n // 2, p)
    return (x * x) % p

def tonelli_shanks(n, p):
    s = 0
    q = p - 1
    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1:
        r = pow_mod(n, (p + 1) // 4, p)
        if (r * r) % p == n:
            return r
        return 0

    # Find the first quadratic non-residue z by brute-force search
    z = 1
    while pow_mod(z, (p - 1) // 2, p) != p - 1:
        z += 1

    c = pow_mod(z, q, p)
    r = pow_mod(n, (q + 1) // 2, p)
    t = pow_mod(n, q, p)
    m = s

    while t != 1:
        tt = t
        i = 0
        while tt != 1:
            tt = (tt * tt) % p
            i += 1
            if i == m:
                return 0

        b = pow_mod(c, pow_mod(2, m - i - 1, p - 1), p)
        b2 = (b * b) % p
        r = (r * b) % p
        t = (t * b2) % p
        c = b2
        m = i

    if (r * r) % p == n:
        return r
    return 0

def solving_congruence(a, b, n):
    d = euclid_algorithm(a, n)
    if b % d != 0:
        return "No solution"
    a //= d
    b //= d
    n //= d
    a_inv = modular_inverse(a, n)
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


def solution_a(a, n):
    congruences = {}
    for factor, occurrence in prime_factor(n).items():
        if occurrence == 2:
            tmp = compute_square_root_order_2(a, factor)
            congruences[factor*factor] = tmp
        else:
            tmp = compute_square_root(a, factor)
            congruences[factor] = tmp
    congruences_list = [(residue, modulus) for modulus, residue in congruences.items()]
    return chinese_remainder(congruences_list)

def solution_b(n, p):
    m = n
    while (n >= p):
        n -= p
    
    tmp = solution_a(n, p)
    a = 2*tmp*p

    while (m >= p*p):
        m -= p*p
    b = m - tmp*tmp

    # find h
    h = solving_congruence(a, b, p*p)
    return tmp + h*p

# Output:
# Question a): a = 492, n = 2023
print(solution_a(492, 2023))
# Question b): a = 492, n = 2023*2023
print(solution_b(492, 2023))
