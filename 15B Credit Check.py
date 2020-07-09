def check(S):
   if len(S)!=19: return False
   for i in range(19):
       if i==4 or i==9 or i==14: 
           if S[i]!=" ":
                return False
       else:
           if S[i].isdigit()==False:
              return False
          # else: 
   temp= S.replace(" ","")
   x=0
   for i in range(16):
     x=x+int(temp[i-3])
   if x %10 !=0: return False
   else: return True
