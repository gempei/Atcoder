N = int(input())
al = map(int,input().split())

denomi = 0
for a in al:
    denomi += 1/a

print(1/denomi)

