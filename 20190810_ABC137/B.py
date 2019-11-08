K,X = map(int,input().split())
maxlim = 1000000
minlim = -1000000
minx = X-K
maxx = X+K
ans_l = [str(i) for i in range(minx+1,maxx)]
print(" ".join(ans_l))

