s = input()
i = len(s) 
firstC = int(0)
secondC = int(1)
valueStore1 = int(0)
valueStore2 = int(0)
for x in range(0, i):
   if s[firstC:secondC] == "+":
      valueStore1 = s[0:secondC-1]
      valueStore2 = s[secondC:i]
      print(int(valueStore1) + int(valueStore2))
      break
   firstC = firstC +1
   secondC=secondC+1
