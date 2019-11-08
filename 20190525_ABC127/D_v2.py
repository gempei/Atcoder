import bisect

def main():
    cardnum,openum = [int(element) for element in input().split(" ")]
    cards = sorted([int(card) for card in input().split(" ")])
    total_change = 0
    for i in range(openum):
        maxchangenum,changevalue  =  [int(element) for element in input().split(" ")]
        total_change += maxchangenum
        index = bisect.bisect_left(cards,changevalue)
        for k in range(maxchangenum):
            cards.insert(index,changevalue)

    cards = cards[total_change:]
    print(sum(cards))


if __name__ == '__main__':
    main()
