import itertools
import bisect

N = int(input())
l_list = sorted(list(map(int,input().split())))
ans = 0

for i in range(N):
    for j in range(i+1,N):
        comb = [l_list[i],l_list[j]]
        minlen = max(comb) - min(comb)
        maxlen = comb[0] + comb[1]
        minindex = bisect.bisect_right(l_list[j+1:],minlen)
        maxindex = bisect.bisect_left(l_list[j+1:],maxlen)
        ans += maxindex - minindex

print(ans)

        
        
