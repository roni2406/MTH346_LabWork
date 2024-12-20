import math

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

result = find_discrete_log(37, 235, 2027)
print(result)