def restricted_extended_euclidean(a, b):        
    # Initialize variables as per algorithm
    r, r_prime = a, b
    s, s_prime = 1, 0
    t, t_prime = 0, 1
    
    # Main loop continues while r_prime != 0
    while r_prime != 0:
        # Calculate quotient and remainder
        q = r // r_prime
        r_double_prime = r % r_prime
        
        # Update values
        r, s, t, r_prime, s_prime, t_prime = (
            r_prime, s_prime, t_prime,
            r_double_prime, s - s_prime * q, t - t_prime * q
        )
    
    # Final GCD is in r
    d = r
    
    return (d, s, t)

def extended_euclidean_unrestricted(a, b):
    sign_a = 1 if a >= 0 else -1
    sign_b = 1 if b >= 0 else -1
    abs_a = abs(a)
    abs_b = abs(b)
    
    d, s, t = restricted_extended_euclidean(abs_a, abs_b)
    return (d, s * sign_a, t * sign_b)
    
# Test the function
d, s, t = restricted_extended_euclidean(-150, 0)
print(f"GCD: {d}, s: {s}, t: {t}")
d, s, t = extended_euclidean_unrestricted(-12, -13)
print(f"GCD: {d}, s: {s}, t: {t}")