S = input()
memo={}
for c in S:
    memo.setdefault(c,0)
    memo[c] += 1

if(len(memo)==2):
    for num in memo.values():
        if(num!=2):
            print("No")
            exit(1)
    print("Yes")
else:
    print("No")
