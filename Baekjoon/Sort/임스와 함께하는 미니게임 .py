n,g = input().split(" ")
players = []
for i in range(int(n)):
  a = input()
  players.append(a)
players = set(players)
if g == "Y":
  print(len(players))
elif g == "F":
  print(len(players)//2)
elif g  == "O":
  print(int(len(players)//3))
