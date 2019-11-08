import queue

N,B1,B2,B3 = map(int,input().split())
min_l = []
max_l = []
ans_l = [ [0 for j in range(N)] for i in range(N)]
mask_l = [ [0 for j in range(N)] for i in range(N)]
for _ in range(N):
    min_l.append(list(map(int,input().split())))
for _ in range(N):
    max_l.append(list(map(int,input().split())))

for i in range(N):
    cursum1 = 0
    cursum2 = 0
    cursum3 = 0
    for j in range(N):
        diff3 = B3 - cursum3
        diff2 = B2 - cursum2
        diff1 = B1 - cursum1
        if(min_l[i][j]<=diff3<=max_l[i][j]):
            ans_l[i][j] = diff3
            cursum3  = 0
            cursum2  += diff3
            cursum3  += diff3
        elif(min_l[i][j]<=diff2<=max_l[i][j]):
            ans_l[i][j] = diff2
            cursum2  = 0
            cursum1 += diff2
            cursum3 += diff2
        elif(min_l[i][j]<=diff1<=max_l[i][j]):
            ans_l[i][j] = diff1
            cursum1  = 0
            cursum2 += diff1
            cursum3 += diff1
        else:
            ans_l[i][j] = min_l[i][j]
            cursum3 += min_l[i][j]
            cursum2 += min_l[i][j]
            cursum1 += min_l[i][j]

for i in range(N):
    cursum1 = 0
    cursum2 = 0
    cursum3 = 0
    for j in range(N):
        diff3 = B3 - cursum3
        diff2 = B2 - cursum2
        diff1 = B1 - cursum1
        if(min_l[i][j]<=diff3<=max_l[i][j]):
            ans_l[i][j] = diff3
            cursum3  = 0
            cursum2  += diff3
            cursum3  += diff3
        elif(min_l[i][j]<=diff2<=max_l[i][j]):
            ans_l[i][j] = diff2
            cursum2  = 0
            cursum1 += diff2
            cursum3 += diff2
        elif(min_l[i][j]<=diff1<=max_l[i][j]):
            ans_l[i][j] = diff1
            cursum1  = 0
            cursum2 += diff1
            cursum3 += diff1
        else:
            ans_l[i][j] = min_l[i][j]
            cursum3 += min_l[i][j]
            cursum2 += min_l[i][j]
            cursum1 += min_l[i][j]
#output
for i in range(N):
    print(" ".join(list(map(str,ans_l[i]))))
