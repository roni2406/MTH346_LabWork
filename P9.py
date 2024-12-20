from helper import find_discrete_log


result = find_discrete_log(37, 235, 2027)
print("x that satisfies 37^x \u2261 235 (mod 2027) is:", result)