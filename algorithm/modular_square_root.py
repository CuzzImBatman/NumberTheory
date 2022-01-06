def pow1(base, exponent, modulus):
     
    result = 1;
    base = base % modulus;
    while (exponent > 0):
        if (exponent % 2 == 1):
            result = (result * base) % modulus;
        exponent = int(exponent) >> 1;
        base = (base * base) % modulus;
 
    return result;
    
def legendre_symbol(a, p):
    ls = pow1(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def modular_square_root(a, p):
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow1(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow1(a, (s + 1) // 2, p)
    b = pow1(a, s, p)
    g = pow1(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow1(t, 2, p)

        if m == 0:
            return x

        gs = pow1(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


if __name__=="__main__":
    print(modular_square_root(223, 17)) # should return 6