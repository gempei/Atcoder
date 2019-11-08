import math

N = int(input())
sl = []

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans_d = {}
ans = 0
for _ in range(N):
    sl.append(input())


for s in sl:
    key = "".join(sorted(s))
    if(key not in ans_d.keys()):
        ans_d[key] = 1
    else:
        ans_d[key] += 1


print(sum([combinations_count(ans,2) for ans in ans_d.values() if ans>1]))

