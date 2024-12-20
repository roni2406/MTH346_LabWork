# Jacobi symbol algorithm
def Jacobi(a, n):
    sigma = 1

    while True:
        a = a % n
        if a == 0:
            if n == 1:
                return sigma
            else:
                return 0            
        h = 0
        while a % 2 == 0:
            h += 1
            a //= 2
            
        # Quadratic reciprocity for powers of 2
        if h % 2 == 1 and n % 8 not in [1, 7]:
            sigma = -sigma
            
        # Quadratic reciprocity
        if a % 4 != 1 and n % 4 != 1:
            sigma = -sigma
            
        # Swap and continue
        a, n = n, a

# Test
print(Jacobi(1983, 2027))
print(Jacobi(873, 2029))
print(Jacobi(474993, 1003001)) 
print(Jacobi(492, 2023*2023))
print(Jacobi(87, 2039))