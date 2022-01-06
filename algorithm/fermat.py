import sys


def mods(a, m):
    if m <= 0:
        return "negative modulus"
    a = a % m
    if 2 * a > m:
        a -= m
    return a


def powmods(a, r, m):
    ## Calculate a^r mod m
    out = 1
    while r > 0:
        if (r % 2) == 1:
            r -= 1
            out = mods(out * a, m)
        r //= 2
        a = mods(a * a, m)
    return out


def quos(a, n):
    if n <= 0:
        return "negative modulus"
    return (a - mods(a, n)) // n


def grem(w, z):
    # remainder in Gaussian integers when dividing w by z
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    if n == 0:
        return "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return (w0 - z0 * u0 + z1 * u1, w1 - z0 * u1 - z1 * u0)


def ggcd(w, z):
    while z != (0, 0):
        w, z = z, grem(w, z)
    return w


def root4(p):
    # 4th root of 1 modulo p
    if p <= 1:
        return "too small"
    if (p % 4) != 1:
        return "not congruent to 1"
    k = p // 4
    j = 2
    while True:
        a = powmods(j, k, p)
        b = mods(a * a, p)
        if b == -1:
            return a
        if b != 1:
            return "not prime"
        j += 1


def sq2(p):
    a = root4(p)
    return ggcd((p, 0), (a, 1))


# Input by command line argument or change variable
input = 97
print(sq2(int(sys.argv[1]) if len(sys.argv) > 1 else input))
