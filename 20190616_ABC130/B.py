N,X = map(int,input().split(" "))
L_l = map(int,input().split(" "))
pos = 0
for i,L in enumerate(L_l):
    pos += L
    if(pos>X):
        print(i+1)
        exit(0)

print(i+2)

