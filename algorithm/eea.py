def eea(a:int, b:int):
    if a == 0:
        return b, 0, 1
    else:
        d, x, y = eea(b%a, a)
        return d, y - (b//a) * x, x

if __name__=="__main__":
    d, x, y = eea(0, 49)
    print('The GCD is', d)
    print(f'x = {x}, y = {y}')

    d, x, y = eea(10, 0)
    print('The GCD is', d)
    print(f'x = {x}, y = {y}')

    d, x, y = eea(34, 27)
    print('The GCD is', d)
    print(f'x = {x}, y = {y}')

    d, x, y = eea(42, 48)
    print('The GCD is', d)
    print(f'x = {x}, y = {y}')