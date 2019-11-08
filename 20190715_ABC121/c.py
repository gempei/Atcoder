def main():
    N,M = map(int,input().split())
    store_l = []
    for i in range(N):
        store_l.append(tuple(map(int,input().split())))

    store_l = sorted(store_l,key=lambda x:x[0])
    ans = 0
    buynum = 0
    for price,maxnum in store_l:
        if(buynum+maxnum<=M):
            buynum += maxnum
            ans += maxnum*price
        else:
            ans += (M-buynum)*price
            break
    print(ans)

if __name__=="__main__":
    main()
