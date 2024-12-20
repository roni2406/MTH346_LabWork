def euclidAlgorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # 3 a)
    r = euclidAlgorithm(20212019, 909431371)
    print ("Question 3a")
    print("GCD:", r)

    # 3 b)
    r = euclidAlgorithm(12345678, 2345698)
    print ("Question 3b")
    print("GCD:", r)

    # 3 c)
    r = euclidAlgorithm(12345675, 567895)
    print ("Question 3c")
    print("GCD:", r)