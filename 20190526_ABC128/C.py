import itertools

def main():
    N,M = list(map(int,input().split(" ")))
    light_l = []
    switch_l = [i for i in range(1,N+1)]
    for _ in range(M):
        light_l.append( list(map(int,input().split(" ")))[1:])
    cheak_l = list(map(int,input().split(" ")))
    ans = 0

    for i in range(N+1):
        for switches in list(itertools.combinations(switch_l,i)):
            for j,light in enumerate(light_l):
                if(cheak_l[j] is not (len(set(switches)&set(light)))%2):
                    break
                if(j is len(light_l)-1):
                    ans += 1

    print(ans)

if __name__ == '__main__':
    main()
