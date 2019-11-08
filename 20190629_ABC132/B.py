N = int(input())
pl = list(map(int,input().split(" ")))
ans = 0
for i in range(N-2):
    num_l = pl[i:i+3]
    if(num_l[1]==sorted(num_l)[1]):
        ans += 1

print(ans)
