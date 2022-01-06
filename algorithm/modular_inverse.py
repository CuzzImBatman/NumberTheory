from eea import eea

def modular_inverse(a, n):
    d, x, y = eea(a, n)
    if d != 1:
        return None
    else:
        return x

if __name__=="__main__":
    print(modular_inverse(13, 22))
    print(modular_inverse(38,97))
    print(modular_inverse(5,3))