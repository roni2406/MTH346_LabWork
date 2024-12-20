import math 

def effective_fermat(p: int):
  if p % 4 != 1 and p != 2:
    return -1, -1
  for i in range(int(math.sqrt(p) + 1)):
    b_sq = p - i ** 2
    b = int(math.sqrt(b_sq))
    if b * b == b_sq:
      return i, b
  return -1, -1
primes = [2053, 3000017, 1234567913]

for p in primes:
  a, b = effective_fermat(p)
  if a == -1 and b == -1:
    print("There is no result for", p)
  else:
    print("The result for p", p, "is a:", a, "b:", b)