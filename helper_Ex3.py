from helper import euclid_algorithm
if __name__ == "__main__":
    # 3 a)
    r = euclid_algorithm(20212019, 909431371)
    print ("Question 3a")
    print("GCD:", r)

    # 3 b)
    r = euclid_algorithm(12345678, 2345698)
    print ("Question 3b")
    print("GCD:", r)

    # 3 c)
    r = euclid_algorithm(12345675, 567895)
    print ("Question 3c")
    print("GCD:", r)
    print(euclid_algorithm(136, 187))