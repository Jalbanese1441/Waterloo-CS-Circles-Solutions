x=input()
if x[len(x)-1]=="C":
    t=str((float(x[0:len(x)-1])*9/5)+32)
    print(t+"F")
if x[len(x)-1]=="F":
    t=str((float(x[0:len(x)-1])-32)*5/9)
    print(t+"C")
