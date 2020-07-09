ST=input()
#ST="01:30"
D=int(input())
#D=30
ST=ST.split(":")
H=int(ST[0])
M=int(ST[1])+D
#print(M)
if M>=60:
   if M%60==0:
      H=H+(M//60)
      M=0
   else:
      H=H+(M//60)
      M=0+(M%60)
#print(H)
if H>=24:
   if H%24==0:
      if H==24: H=0
      else:
         H=0+(H//24)
   else:
      H=0+(H%24)	
#print(H)
M=str(M)
H=str(H)
if len(H)!=2:
   H="0"+H
if len(M)!=2:
   M="0"+M
H=H+":"
ST=H+M
print(ST)
