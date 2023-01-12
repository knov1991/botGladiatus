def coord():
  try:
    x = 1
    y = 2
    open('aaa.txt')
    return x,y
  except:
    return []


print(len(coord()))