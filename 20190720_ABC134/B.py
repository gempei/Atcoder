N,D = map(int,input().split())
q,mod = divmod(N,(2*D+1))
if(mod!=0):
    print(q+1)
else:
    print(q)
