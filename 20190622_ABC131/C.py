def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

A,B,C,D = map(int,input().split(" "))
min_C = B//C-(A-1)//C
min_D = B//D-(A-1)//D
lcm = lcm(C,D)
min_lcm = B//lcm-(A-1)//lcm
print(B-A-min_C-min_D+min_lcm+1)

