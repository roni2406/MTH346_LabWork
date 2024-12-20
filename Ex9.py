from math import sqrt, ceil

def powmod(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

def solve(a, b, m):
    a %= m
    b %= m
    n = ceil(sqrt(m))
    
    # Store giant steps
    vals = {}
    for p in range(1, n + 1):
        val = powmod(a, p * n, m)
        vals[val] = p
    
    # Check baby steps
    for q in range(n + 1):
        cur = (powmod(a, q, m) * b) % m
        if cur in vals:
            ans = vals[cur] * n - q
            return ans
            
    return -1

# Test
print(solve(2, 3, 5))