def findLine(prog, target):
    for i in range(len(prog)):
      splited=prog[i].split()
      if splited[0]==str(target):
          return i
def execute(prog):
  location = 0
  i=10
  visited=[False]*len(prog)
  for i in range(len(prog)):
    if location==len(prog)-1: return "success"
    temp=(prog[location].split())
    T=temp[2]
    if visited[location]==True: return "infinite loop"
    visited[location]=True
    location = findLine(prog, T)
    location = findLine(prog, T)
