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

def part_a():
  mod1, r1 = 5 ** 4, 363
  mod2, r2 = 16, 0

  res = chinese_remainder([(r1, mod1), (r2, mod2)])
  return res % 10000

def part_b():
  congruences = [(6789, 12354), (54292, 56789)]
  res = chinese_remainder(congruences)
  return res

def part_c():
  congruences = [(23, 41), (81, 152), (127, 263)]
  res = chinese_remainder(congruences)
  return res

res = part_a()
print("The answer for 7a is", res)

res = part_b()
print("The answer for 7b is", res)

res = part_c()
print("The answer for 7c is", res)