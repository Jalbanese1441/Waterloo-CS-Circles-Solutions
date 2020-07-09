t="" # used to store the input (broken up)
x="" # stores the current line
commonWord=""
previousCount=0
while x!="###":
    x=input()
    x=x.lower()
    t= t+" "+x
y=t.split()
for i in range(len(y)):
   # print(i,y[i],y.count(y[i]))   
    if y.count(y[i]) >previousCount:
        previousCount=y.count(y[i])
        commonWord=y[i]
print(commonWord)
