A,B = map(int,input().split())
x,y,z = A-B ,A+B,A*B
print(max([x,y,z]))
