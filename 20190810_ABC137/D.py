from pprint import pprint
N,M = map(int,input().split())
bl = []

for _ in range(N):
    days,money = map(int,input().split())
    bl.append([days,money,money/days])

bl = sorted(bl,key=lambda x:-x[1])
spenddays = 0
dl = []
ans_l = 0
for b in bl:
    cond_spenddays = max(spenddays,b[0]+(dl+[b[0]]).count(b[0])-1)
    if(cond_spenddays<=M):
        dl.append(b[0])
        ans += b[1]
        spenddays = cond_spenddays

print(ans)
