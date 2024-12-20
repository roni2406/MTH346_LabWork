from helper import euclid_algorithm
if __name__ == "__main__":
    # 3 a)
    r = euclid_algorithm(20212019, 909431371)
    print ("Question 3a: GCD of 20212019 and 909431371 is: " + str(r))

    # 3 b)
    r = euclid_algorithm(12345678, 2345698)
    print ("Question 3b: GCD of 12345678 and 2345698 is: " + str(r))

    # 3 c)
    r = euclid_algorithm(12345675, 567895)
    print ("Question 3c: GCD of 12345675 and 567895 is: " + str(r))