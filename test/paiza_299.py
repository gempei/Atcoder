def main():
    p1,p2,p3,k = map(int,input().split())
    pl = sorted([p1,p2,p3])[::-1]

    ans_l = []
    q1,r1 = divmod(p1,p2)
    q2,r2 = divmod(p1,p3)
    q3,r3 = divmod(p2,p3)

    numl = [p1,p2,p3]
    dp = [[0 for i in range(10005)] for j in range(10005)]
    while(len(numl)<=5*k):
        tmpl = []
        for i in range(len(numl)):
            for j in range(len(numl)):
                if(dp[i][j]==0):
                    tmp = numl[j]*numl[i]
                    tmpl.append(tmp)
                    dp[i][j]=tmp

        numl = numl+list(set(tmpl))

    print(sorted([1]+list(set(numl)))[k-1])

if __name__=="__main__":
    main()
