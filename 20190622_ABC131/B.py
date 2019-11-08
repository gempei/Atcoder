N,L = map(int,input().split(" "))
ans = 0
absmin = 300
for i in range(N):
    taste = i+L
    ans+=taste
    if(abs(taste)<abs(absmin)):
        absmin = taste
print(ans-absmin)
