from helper import effective_fermat
primes = [2053, 3000017, 1234567913]

print("Question 5: ")
for p in primes:
  a, b = effective_fermat(p)
  if a == -1 and b == -1:
    print("There is no result for", p)
  else:
    print("The result for p =", p, "is a =", a, "and b =", b)
print(" ")