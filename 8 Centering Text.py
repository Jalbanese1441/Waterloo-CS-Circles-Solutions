width = int(input())
x=[]
y=""
while y!="END":
   y=input()
   x.append(y)
x.remove("END")
for i in range(len(x)):
   spaceLeft=width-len(x[i])
   if spaceLeft!=0:
      if spaceLeft%2==0:
         LS=spaceLeft/2
         RS=LS
      else:
         LS=spaceLeft//2+spaceLeft%2
         RS=(spaceLeft-LS)
      LS=int(LS)
      RS=int(RS)
      print("."*LS+x[i]+"."*RS)
   else: print(x[i])
