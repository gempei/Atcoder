N,K,Q = map(int,input().split())
A_l = []
for _ in range(Q):
  A_l.append(int(input()))

must = Q - K + 1
part_l = [0 for _ in range(N)]

for A in A_l:
  part_l[A-1] += 1

for part in part_l:
  if(part<must):
    print("No")
  else:
    print("Yes")
