N,M = map(int,input().split())
city_d = {}
ans_l = ["" for _ in range(M)]
for i in range(M):
    P,Y = map(int,input().split())
    city_d.setdefault(P,[])
    city_d[P].append([Y,i])

for p,y_orgnum in city_d.items():
    for j,sorted_y_orgnum in enumerate(sorted(y_orgnum,key=lambda x:x[0])):
        ans_l[sorted_y_orgnum[1]] = str(p).zfill(6) + str(j+1).zfill(6)

for ans in ans_l:
    print(ans)


