N = int(input())
ml = list(map(int,input().split()))
hl = list(map(int,input().split()))
ans = 0

for i,h in enumerate(hl):
    if(ml[i]<h):
        ans += ml[i]
        h -= ml[i]
        ml[i] = 0
        if(ml[i+1]<h):
            ans += ml[i+1]
            h -= ml[i+1]
            ml[i+1] = 0
        else:
            ans += h
            ml[i+1] -= h
            h = 0
    else:
        ans += h
        ml[i] -= h
        h = 0

print(ans)
