def prod(L):
   result=int(1)
   for i in range(len(L)):
      result=result*L[i-1]
   return result
