a,b = map(int,input().split())
q,r = divmod(a+b,2)
if(r==1):
    print("IMPOSSIBLE")
else:
    print(q)
