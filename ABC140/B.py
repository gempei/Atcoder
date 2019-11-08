N = int(input())
A_l = list(map(int,input().split()))
B_l = list(map(int,input().split()))
C_l = list(map(int,input().split()))

ans = 0
for i in range(N-1):
    ans += B_l[A_l[i]-1]
    if(A_l[i]+1 == A_l[i+1]):
        ans += C_l[A_l[i]-1]
ans += B_l[A_l[N-1]-1]
print(ans)
