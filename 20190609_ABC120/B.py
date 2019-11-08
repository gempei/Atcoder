def main():
    N = int(input())
    Wl = list(map(int,input().split(" ")))

    ansmin = sum(Wl)
    for i in range(N):
        sum1 = sum(Wl[:i])
        sum2 = sum(Wl[i:])
        condmin = abs(sum1-sum2)
        if(condmin<ansmin):
            ansmin = condmin

    print(ansmin)

if __name__ == "__main__":
    main()

