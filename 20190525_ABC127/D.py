import bisect

def main():
    cardnum,openum = [int(element) for element in input().split(" ")]
    cards = sorted([int(card) for card in input().split(" ")])

    for i in range(openum):
        maxchangenum,changevalue  =  [int(element) for element in input().split(" ")]
        changenum = 0
        for j in range(maxchangenum):
            if(cards[j]<changevalue):
                changenum += 1
            else:
                break
        cards = cards[changenum:]
        index = bisect.bisect_left(cards,changevalue)
        for k in range(changenum):
            cards.insert(index,changevalue)

    print(sum(cards))


if __name__ == '__main__':
    main()
