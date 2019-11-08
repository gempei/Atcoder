N = int(input())
stairs = list(map(int,input().split()))

if(N>2):
    dp = [0,abs(stairs[1]-stairs[0]),abs(stairs[2]-stairs[0])]
else:
    dp = [0,abs(stairs[1]-stairs[0])]

for i in range(3,N):
    cond1 = abs(stairs[i]-stairs[i-1]) + dp[i-1]
    cond2 = abs(stairs[i]-stairs[i-2]) + dp[i-2]
    dp.append(min(cond1,cond2))

print(dp[-1])

