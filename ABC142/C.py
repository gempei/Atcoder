N = int(input())
Al = list(map(int,input().split()))
sd = {}
for i,A in enumerate(Al):
    sd[str(i+1)] = A

ans_l = []
for key,value in sorted(sd.items(),key=lambda x:x[1]):
    ans_l.append(key)

print(" ".join(ans_l))



