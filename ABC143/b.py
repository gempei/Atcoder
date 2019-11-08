N = int(input())
dl = list(map(int,input().split()))

ans = 0
for i in range(len(dl)):
    for j in range(i+1,len(dl)):
        ans += dl[i]*dl[j]

print(ans)
