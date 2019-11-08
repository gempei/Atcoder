N,K = map(int,input().split())
nl = list(map(int,input().split()))

MAX= 10**6 if min(nl)+K>10**6 else min(nl)+K
MIN = 1
ans = -1

for i in range(1,MAX):
    tmp_l = []
    for n in nl:
        q,r = divmod(n,i)
        tmp_l.append(r)
    if(sum(tmp_l)==0):
        ans = i

print(ans)

