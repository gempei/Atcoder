N,Q = map(int,input().split())
S = input()
qlist = [map(int,input().split()) for _ in range(Q)]
tarstr = "AC"
dp = []
maxnum = 0
flg = False
for c in S:
    if(c=="A"):
        flg = True
    elif(c=="C" and flg):
        maxnum += 1
        flg = False
    else:
        flg = False
    dp.append(maxnum)

for l,r in qlist:
    print(dp[r-1]-dp[l-1])

