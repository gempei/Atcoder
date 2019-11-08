def cheaker(orgstr,compstr):
    for i,c in enumerate(orgstr):
        if(c!="?"):
            if(c!=compstr[i]):
                return False
    return True



S = input()
d = len(S)
print(d)
r = 5
q = 13
ans = 0
ansmod = 10**9 +7

for i in range(10**d//q):
    tarstr = str(q*i+r).zfill(d)
    print(tarstr)
    if(cheaker(S,tarstr)):
        ans += 1
        ans %= ansmod

print(ans)
