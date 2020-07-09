isPrime = [True] * 1000001

def isPrime2(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def isItPrime(N):
    for i in range(0, len(N)):
        if not isPrime2(i): N[i] = False

isItPrime(isPrime)


#N=1000001
#isPrime=[True]*N
#print(round(math.sqrt(N)))
#for i in range(2,round(math.sqrt(N))):
#for x in range(2,N+1):
#   for i in range(N+1):
        #print(i)
       # if i%x==0 and i!=x:
        # print(isPrime[i])
          #  isPrime[i]=False
#isPrime[0]=False
#isPrime[1]=False