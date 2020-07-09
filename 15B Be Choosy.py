Be Choosyimport math
def choose(n, k):
   x=math.factorial(n)
   y=math.factorial(n-k)
   y=y*math.factorial(k)
   y=x/y
   return y
