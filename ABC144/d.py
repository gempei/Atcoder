import math
import bisset
a,b,x = map(int,input().split())
radian = 0

while(radian<=45):
    diff = a*a*a*math.tan(math.radians(radian))
    print(diff) 
    radian += 10**-6

    if(abs(x-(a*a*b-diff))<10**-6):
        print(radian)
        exit(0)


