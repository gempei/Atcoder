S = input()
ans_l = [0 for _ in range(len(S))]

"""
for i in range(len(S)):
    if(S[i]=="R"):
        j = 0
        while(S[i+j]=="R"):
            j += 1
        if(j%2==1):
            ans_l[i+j-1]+=1
        else:
            ans_l[i+j]+=1

    if(S[i]=="L"):
        j = 0
        while(S[i-j]=="L"):
            j += 1
        if(j%2==1):
            ans_l[i-j+1]+=1
        else:
            ans_l[i-j]+=1
"""
i =0
while(i<len(S)):
    j=0
    while(S[i+j]=="R"):
        j += 1
    k=0
    while(S[i+j+k]=="L"):
        k += 1
        if(i+j+k>=len(S)):
            break
    ans_l[i+j-1] += j//2+ k//2 + j%2
    ans_l[i+j] += j//2 + k//2 + k%2
    i += j+k


print(" ".join(map(str,ans_l)))

