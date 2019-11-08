N,M = map(int,input().split())
maxcond = N*4
mincond = N*2
if(maxcond < M or mincond > M):
    print("-1 -1 -1")
else:
    b = 0
    c = 0
    a,r = divmod(M,2)
    if(r==1):
        b = 1
        a -= 1

    cheaker = a+b-N
    if(cheaker>0):
        c += cheaker
        a -= cheaker*2
    print(str(a) + " " + str(b) +" " +  str(c))


