import math
import itertools

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N,K = map(int,input().split(" "))
    for i in range(1,K+1):
        if(i<=N-K+1):
            print(combinations_count(K-1,i-1)*combinations_count(N-K+1,i)%(10**9+7))
        else:
            print(0)

if __name__=='__main__':
    main()
