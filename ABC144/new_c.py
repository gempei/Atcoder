def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

N = int(input())

tmp = make_divisors(N)
if(len(tmp)%2==0):
    print((tmp[-1]-1)+(tmp[-2]-1))
else:
    print((tmp[-1]-1)+(tmp[-1]-1))
