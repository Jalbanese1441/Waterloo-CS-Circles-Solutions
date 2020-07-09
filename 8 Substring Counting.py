needle = input()
haystack = input()
c=0
checkL =len(needle)
for i in range(len(haystack)):
   if haystack[i:checkL]==needle: c+=1
   checkL+=1
   
print(c)
