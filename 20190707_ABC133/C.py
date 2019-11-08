L,R = map(int,input().split(" "))
modnum = 2019
if(R-L+1>modnum):
    print(0)
else:
    diff_l = []
    for i in range(L,R+1):
        diff_l.append(i%modnum)
    diff_l = sorted(diff_l)
    print((diff_l[0]*diff_l[1])%modnum)
