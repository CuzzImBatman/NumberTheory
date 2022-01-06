from eea import eea
from modular_inverse import modular_inverse

def crt(a:list, m:list):
    print(a)
    print(m)
    k = len(a)
    x = 0
    for i in range(0,k):
        n = 1
        temp=1
        for j in range(0,k):
            if j != i:
                n *= m[j]
                temp = (temp%m[i])*(m[j]%m[i])
        b = modular_inverse(temp, m[i])
        print(b)
        if b == None: return None
        x += (a[i]% m[i]) * n * b
    return x

if __name__=="__main__":
    #print( crt( (5000000000000000000000000000000000000000000000000,7), (5,3) ) )
    print( crt( (300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004,8000000047980000000009862400000000000000000000001), (35,79) ) )
    