import itertools
from collections import Counter

N = int(input())
l_list = Counter(list(map(int,input().split())))
ans = 0
for comb in  itertools.combinations(l_list.keys(), 3):
    if(comb[0] < comb[1]+comb[2] and comb[1] < comb[0]+comb[2] and comb[2] < comb[1]+comb[0]):
        ans += l_list[comb[0]] * l_list[comb[1]] * l_list[comb[2]]

print(ans)
