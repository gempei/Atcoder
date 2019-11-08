N,K = map(int,input().split())
S = input()

ranlength_l = []
count = 1
if(N==1):
    ranlength_l.append([S[0],1])
else:
    for i in range(1,len(S)):
        if(S[i] != S[i-1]):
            ranlength_l.append([S[i-1],count])
            count = 1
        else:
            count += 1
        if(i==len(S)-1):
            ranlength_l.append([S[len(S)-1],count])

ans = N-len(ranlength_l)
for const in (ranlength_l[1:-1:2]):
    if(K==0):
        break
    ans += 2
    K = K-1

if(K!=0 and len(ranlength_l)!=1):
    ans+=1

print(min([ans,N-1]))


