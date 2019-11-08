N = int(input())
flowers = list(map(int,input().split(" ")))
ans = 0

def is_clear(l):
    for ele in l:
        if(ele!=0):
            return False
    return True

while(not is_clear(flowers)):
    tmp_l = []
    #水やり範囲を決める処理
    for i,flower in enumerate(flowers):
        if(flower!=0):
            tmp_l.append(i)
        else:
            if(len(tmp_l)!=0):
                break


    if(len(tmp_l)>=2):
        water = min(flowers[tmp_l[0]:tmp_l[-1]+1])
        for i in tmp_l:
            flowers[i] -= water
    else:
        water = flowers[tmp_l[0]]
        flowers[tmp_l[0]] -= water

    ans += water

print(ans)
