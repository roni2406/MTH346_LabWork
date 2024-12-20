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

rats = [0.372636, 0.373346671, 0.2173836482]
limit = 10

for r in rats:
  num, denom, terms = best_approx_rational(r, limit)
  print(f"Decimal: {r}")
  print(f"Continued Fraction Terms: {terms}")
  print(f"Fraction: {num}/{denom} = {num / denom}\n")