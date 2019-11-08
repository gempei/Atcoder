N = int(input())
a_l = list(map(int,input().split()))
ans_l = {}
for i,a in enumerate(a_l[::-1]):
    index = N-i
    curnum = 0
    for j in range(2,N//2):
        if(index*j<=N):
           curnum += ans_l[index*j]

    if(curnum%2!=a):
        ans_l[index] = 1
    else:
        ans_l[index] = 0

inlist = []
ans_len = 0
for key,num in ans_l.items():
    if(num==1):
        inlist.append(key)
        ans_len+=1

ans_str = " ".join(list(map(str,sorted(inlist))))
print(ans_len)
if(ans_str != ""):
    print(ans_str)

