from helper import prime_factor, compute_square_root, compute_square_root_order_2, chinese_remainder, solving_congruence

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

# Question a): a = 492, n = 2023
print("Question 10:")
print("x that satisfies x^2 \u2261 492 (mod 2023) is", solution_a(492, 2023))
# Question b): a = 492, n = 2023*2023
print("x that satisfies x^2 \u2261 492 (mod 2023^2) is", solution_b(492, 2023))
