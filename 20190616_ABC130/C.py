W,H,x,y = map(int,input().split(" "))
area = W*H/2
if((float(x)==W/2) and (float(y)==H/2)):
    flag = 1
else:
    flag = 0
print("{} {}".format(str(area),str(flag)))
