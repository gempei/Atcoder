N,K = map(int,input().split(" "))
a_l = map(int,input().split(" "))
sumans = 0
ans = 0
sum_l = []
for a in a_l:
    sumans += a
    sum_l.append(sumans)

for i,x in enumerate(sum_l):
    if(x>K):
        diff = x-K
        for j,y in enumerate(sum_l):
            if(diff<y):
                ans += j+1
                break

print(ans)
