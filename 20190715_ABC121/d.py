a,b = map(int,input().split())
def xor(x):
    return(x,1,x+1,0)[x%4]
print(xor(a-1)^xor(b))
