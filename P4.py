from helper import effective_fermat
primes = [2029, 474993, 1003001]

print("Question 4: ")
for p in primes:
  ans = effective_fermat(p)
  print(f"For p = {p}, m and n such that m^2 + n^2 = p is: {ans}")
print("add +- to the answer to get the solution when a, b are negative")
print(" ")
