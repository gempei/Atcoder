N = int(input())
B_l = list(map(int,input().split()))[::-1]
ans = B_l[0]
for i in range(N-2):
    ans += min([B_l[i],B_l[i+1]])
ans += B_l[len(B_l)-1]

print(ans)
