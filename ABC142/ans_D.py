def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

A,B = map(int,input().split())
minnum,maxnum = sorted([A,B])
div_l = factorization(gcd(minnum,maxnum))

if((div_l[0][0])==1):
    print(len(div_l))
else:
    print(len(div_l)+1)
