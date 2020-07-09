import math
L = float(input())
A = float(input())
for i in range(10):
   x=L*math.cos((A*math.cos(i*(math.sqrt(9.8/L)))))
   print(x-(L*math.cos(A)))
