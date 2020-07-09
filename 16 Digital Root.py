def digitalRoot(n):
   if n < 10: return n
   else:
    x= digitalRoot(digitalSum(n))
    return x
