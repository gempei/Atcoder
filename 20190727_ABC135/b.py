N = int(input())
al = list(map(int,input().split()))
ansal = sorted(al)

for i in range(N):
    for j in range(i,N):
        cond_al = al.copy()
        cond_al[i],cond_al[j] = cond_al[j],cond_al[i]
        if(cond_al==ansal):
            print("YES")
            exit(0)

print("NO")
