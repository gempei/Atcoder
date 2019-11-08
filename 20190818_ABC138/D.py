N,Q = map(int,input().split())
abl = []
ql = []
for _ in range(N-1):
    abl.append(list(map(int,input().split())))
for _ in range(Q):
    ql.append(list(map(int,input().split())))


tree = [[0 for i in range(N)] for _ in range(N)]
for ab in abl:
    tree[ab[0]][ab[1]] = 1

