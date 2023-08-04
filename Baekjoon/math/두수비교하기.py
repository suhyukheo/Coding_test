a,b = input("").split(" ")
c = int(b)-int(a)
if c == 0:
  print("==")
elif c < 0:
  print(">")
elif c>0:
  print("<") 
