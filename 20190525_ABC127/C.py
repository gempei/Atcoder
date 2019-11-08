def main():
    idnum,gatenum = [int(element) for element in input().split(" ")]
    minid = 0
    maxid = idnum

    for gete in range(gatenum):
        condmin,condmax = [int(element) for element in input().split(" ")]
        if(minid<condmin):
            minid = condmin
        if(maxid>condmax):
            maxid = condmax

    if(maxid<minid):
        print(0)
    else:
        print(maxid-minid+1)

if __name__ == "__main__":
    main()
