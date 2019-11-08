N,K = map(int,input().split())
hl = list(map(int,input().split()))
ans = 0
for h in hl:
    if(h>=K):
        ans += 1

print(ans)
