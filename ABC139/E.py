N = int(input())
match_l = []
for _ in range(N):
    match_l.append(list(map(int,input().split())))

day = 0
while(True):
    players = []
    fin_count = 0
    for i,match in enumerate(match_l):
        if(not match):
            fin_count += 1

        elif(i not in players):
            if(match_l[match[0]-1]):
                if(match_l[match[0]-1][0]-1==i):
                    players.append(i)
                    players.append(match[0]-1)

    if(fin_count == N):
        print(day)
        exit(0)
    if(not players):
        print(-1)
        exit(0)

    for player in players:
        match_l[player].pop(0)

    day += 1

