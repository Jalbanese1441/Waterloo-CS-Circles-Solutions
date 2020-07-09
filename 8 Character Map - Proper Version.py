s="asc: "
sc= "chr:  "
for i in range(32,129):
   if (i)%16 == 0:
      if i>34:
         print(sc)
         print(s)
      s= "asc: "
      sc= "chr:  "
   if i>= 100:s+=str(i)+" "
   else:s+=str(i)+"  "
   sc+=chr(i)+"   "