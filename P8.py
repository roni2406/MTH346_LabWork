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

def solution_c(n, p):
    m = n
    while (n >= p):
        n -= p
    
    tmp = solution_b(n, p)
    a = 2*tmp*p*p

    while (m >= p*p*p):
        m -= p*p*p
    b = m - tmp*tmp

    # find h
    h = solving_congruence(a, b, p*p*p)
    return tmp + h*p*p

print("Question 8:")
# Output:
# Question a): a = 448, b = 673
print("x that satisfies x^2 \u2261 448 (mod 673) is", solution_a(3, 2003))
# Question b): a = 448, b = 673*673
print("x that satisfies x^2 \u2261 448 (mod 673^2) is", solution_b(3, 2003))
# Question c): a = 448, b = 2019*2019*2019
print("x that satisfies x^2 \u2261 448 (mod 2019^3) is", solution_c(448, 2019))