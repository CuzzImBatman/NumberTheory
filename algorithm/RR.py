
def RR(c:float,k):
    temp= str(c)
    temp=temp[2:]
    a= int(temp)
    b=1
    A=a
    while A > 0:
        A= A//10
        b*=10
    #print(str(a)+ " " + str(b))
    s0 ,s1, s2=1 ,0,0
    t0 ,t1, t2=0 ,1,0
    if a == 0:
        return  0, 1
    if b == 0:
        return  1, 0
    while True:
        q=a//b
        r= a%b
        if r==0:
            break
        a=b
        b=r
        s2= s0- q*s1
        t2= t0 -q*t1
        if (s2 >k) | (t2 > k):
            s2=s1
            t2=t1
            break
        #print(str(q)+ " " + str(r))
        #print(str(s0) +" "+ str(s1) + " " + str(s2))
        #print(str(t0) +" "+ str(t1) + " " + str(t2))
        
        s0=s1
        s1= s2
        t0=t1
        t1= t2
    return s2,t2    

x,y = RR(0.7197183098591549,1000)
x= abs(x)
y= abs(y)

print(min(x,y))
print(max(x,y))