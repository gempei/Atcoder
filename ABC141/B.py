S = input()

for i,c in enumerate(S):
  if(i%2==1):
    if(c not in ["L","U","D"]):
      print("No")
      exit(0)
  else:
    if(c not in ["R","U","D"]):
      print("No")
      exit(0)

print("Yes")
