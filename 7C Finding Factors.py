n = int(input())
c = int(1)
t = int(0)
for i in range(1, n + 1):
       if n % i == 0:
         t = int(n/i)
         print(i, "times", t, "equals", n)
