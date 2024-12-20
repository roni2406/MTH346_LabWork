def extendEuclideanAlgorithm(a, b):
    s = 1
    s1 = 0
    t = 0
    t1 = 1
    r = a
    r1 = b
    
    while (r1 != 0):
        q = r // r1
        r2 = r % r1
        s2 = s - q * s1
        t2 = t - q * t1
        r = r1
        s = s1
        t = t1
        r1 = r2
        s1 = s2
        t1 = t2
    
    
    return r, s, t

def modularInverse(a, m):
    r, s, t = extendEuclideanAlgorithm(a, m)
    if (r != 1):
        return None
    else:
        while (s < 0):
            s += m
        return s


if __name__ == "__main__":
    # 4 a)
    r, s, t = extendEuclideanAlgorithm(1234567892, 197654321)
    print ("Question 4a")
    print("s:", s)
    print("t:", t)

    # 4 b)
    print ("Question43b")
    r = modularInverse(37, 2023)
    if (r != None):
        print("Inverse: ", r)
    else:
        print("No inverse")
    
