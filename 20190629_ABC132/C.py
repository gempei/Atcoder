N = int(input())
diff_l = sorted(list(map(int,input().split(" "))))

qnum = len(diff_l)
if(qnum%2!=0):
    print(0)
else:
    print(diff_l[int(qnum/2)]-diff_l[int(qnum/2-1)])

