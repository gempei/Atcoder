A,B = map(int,input().split())

curnum = 1
ans = 0
while(B>curnum):
    curnum += A-1
    ans += 1

print(ans)

