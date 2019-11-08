N = int(input())
a_d = {}
for i in range(N):
    a_d[i] = int(input())

sorted_a_d = sorted(a_d.items(),key=lambda x:-x[1])
for i in range(N):
    if(sorted_a_d[0][0]!=i):
        print(sorted_a_d[0][1])
    else:
        print(sorted_a_d[1][1])


