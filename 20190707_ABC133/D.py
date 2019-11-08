import numpy as np
import itertools

#mat = np.array([[1.,1.,0.], [0., 1.,1.], [1.,0.,1.]])
#b = np.array([4., 4., 8.])
N = int(input())
a_l = [i*2 for i in list(map(float,input().split(" ")))]
mat_l = []
for i in range(N):
    mat_l.append([1. if (j==i or j==(i+1)%(N)) else 0. for j in range(N)])
mat=np.array(mat_l)
b=np.array(a_l)

for i in range(len(mat)-1):
    for j in range(i+1, len(mat)):
        coef = mat[j][i] / mat[i][i]
        mat[j] -= mat[i] * coef
        b[j] -= b[i] * coef

for i in range(len(mat)-1, 0, -1):
    b[i] /= mat[i][i]
    mat[i] /= mat[i][i]
    for j in range(i):
        b[j] -= b[i] * mat[j][i]
        mat[j][i] = 0

ans_str=""
for i,ans in enumerate(b):
    if(i!=len(b)-1):
        ans_str+=str(int(ans))+" "
    else:
        ans_str+=str(int(ans))

print(ans_str)
