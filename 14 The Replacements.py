def replace(list, X, Y):
   while list.count(X)>0:
      list.insert(list.index(X),Y)
      list.remove(X)
