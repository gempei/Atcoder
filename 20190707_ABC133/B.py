import itertools
import math
def distance(v1,v2):
    if(len(v1)!=len(v2)):
        return False
    distance = 0
    for i in range(len(v1)):
        distance+=(v2[i]-v1[i])**2
    return math.sqrt(distance)


N,D = map(int,input().split(" "))
plots=[]
for i in range(N):
    plots.append(list(map(int,input().split(" "))))

comb_l = list(itertools.combinations([i for i in range(N)],2))
ans = 0
for comb in comb_l:
    if(distance(plots[comb[0]],plots[comb[1]]).is_integer()):
        ans+=1

print(ans)

