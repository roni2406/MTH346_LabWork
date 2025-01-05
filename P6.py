from helper import chinese_remainder


def part():
  congruences = [(3, 8), (8, 11), (11, 23)]
  res = chinese_remainder(congruences)
  return res

print("Question 6:")
res = part()
print("The remainder when divide A by 2024 is", res % 2024, "\n")