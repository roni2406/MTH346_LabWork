from helper import best_approx_rational

rats = [0.372636, 0.373346671, 0.2173836482]
limit = 10

print("Question 6: ")
for r in rats:
  num, denom, terms = best_approx_rational(r, limit)
  print(f"Decimal: {r}")
  print(f"Continued Fraction Terms: {terms}")
  print(f"Fraction: {num}/{denom} = {num / denom}\n")