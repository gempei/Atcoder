N = int(input())
hl = list(map(int,input().split()))

hl[0] = hl[0]-1
for i in range(1,N-1):
    if(hl[i]>hl[i-1]):
        hl[i] = hl[i]-1
    if(hl[i]>hl[i+1]):
        print("No")
        exit(0)

print("Yes")

