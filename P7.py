from helper import chinese_remainder

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

print("Question 7:")
res = part_a()
print("The answer for 7a is", res)

res = part_b()
print("The answer for 7b is", res)

res = part_c()
print("The answer for 7c is", res, "\n")