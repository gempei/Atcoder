N = int(input())
h_l = list(map(int,input().split()))

continious = 0
ans = 0
for i in range(N-1):
    if(h_l[i+1]<=h_l[i]):
        continious += 1
    else:
        ans = max([ans,continious])
        continious = 0

ans = max([ans,continious])
print(ans)


