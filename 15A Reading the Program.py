def getBASIC():
    holder=[]
    x=""
    while x.endswith("END")==False:
       x=input()
       holder.append(x)
    return holder
