import itertools
from collections import Counter

N = int(input())
l_list = Counter(list(map(int,input().split())))
print(l_list)
ans = 0
for comb in  itertools.combinations(l_list.keys(), 2):
    maxlen = comb[0] + comb[1]
    minlen = max(comb)-min(comb)
    for k,v in l_list.items():
        if(k<maxlen and k>minlen and k!=comb[0] and k!=comb[1]):
            print(comb)
            print(k)
            ans += v
    """
    for l in comb:
        if(l<maxlen and l>minlen):
            ans -= l_list[l]
    print()
    """

print(ans)
