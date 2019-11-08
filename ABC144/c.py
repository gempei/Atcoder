def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())

ele_l = factorization(N)
new_ele_l = []
for ele in ele_l:
    new_ele_l.extend([ele[0]]*ele[1])

if(len(new_ele_l)<2):
    new_ele_l.append(1)
#print(ele_l)
#print(new_ele_l)
while(len(new_ele_l)>2):
    update_ele = new_ele_l[0]*new_ele_l[1]
    new_ele_l = new_ele_l[2:]
    #print(new_ele_l)
    new_ele_l.append(update_ele)
    new_ele_l = sorted(new_ele_l)
    #print(new_ele_l)

print((new_ele_l[0]-1)+(new_ele_l[1]-1))
