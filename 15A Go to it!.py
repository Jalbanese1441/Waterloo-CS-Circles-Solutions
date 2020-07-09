def findLine(prog, target):
    for i in range(len(prog)):
      splited=prog[i].split()
      if splited[0]==str(target):
          return i
