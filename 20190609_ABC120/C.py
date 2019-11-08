import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def stairs(n):
    if(n<=0):
        return 1
    comb = 0
    for i in range(int(n/2)+1):
        comb += combinations_count(n-i,i)
    return comb

def main():
    N,M = map(int,input().split(" "))
    broken_l = []
    for _ in range(M):
        broken_l.append(int(input()))

    broken_l.append(-1)
    broken_l.append(N+1)
    broken_l.sort()
    ans = 1
    for i in range(len(broken_l)-1):
        step = broken_l[i+1] - broken_l[i]
        if(step == 1 and broken_l[i+1]!=1):
            print(0)
            exit(0)
        else:
            ans *= stairs(step-2)
            ans = ans%(10**9+7)

    print(ans)
if __name__ == '__main__':
    main()
