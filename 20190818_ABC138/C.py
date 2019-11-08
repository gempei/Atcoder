N = int(input())
vl =list(map(int,input().split()))
ans = 0

for i,v in enumerate(sorted(vl)):
    if(i==0):
        ans +=  v/(2**(N-1))
    else:
        ans +=  v/(2**(N-i))

print(ans)
