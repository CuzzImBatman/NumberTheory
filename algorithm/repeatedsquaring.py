import sys


def mods(a, m):
    if m <= 0:
        return "negative modulus"
    a = a % m
    if 2 * a > m:
        a -= m
    return a


def powmods(a, e, n):
    ## Calculate a^e mod n
    out = 1
    while e > 0:
        if (e % 2) == 1:
            e -= 1
            out = mods(out * a, n)
        e //= 2
        a = mods(a * a, n)
    return out


a = 123
e = 12345678
n = 10

if len(sys.argv) != 4:
    print(powmods(a, e, n))
else:
    print(powmods(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
