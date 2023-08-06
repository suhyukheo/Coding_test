while True:
  a,b,c = input().split(" ")
  a,b,c = int(a),int(b),int(c)
  if a == 0 and b ==0 and c == 0:
    break 
  sort_list = [a,b,c]
  sort_list.sort(reverse=True)
  if sort_list[0] >= sort_list[1]+sort_list[2]:
    print("Invalid")
  elif sort_list[0] == sort_list[1] == sort_list[2]:
    print("Equilateral")
  elif sort_list[0] == sort_list[1] or sort_list[1] == sort_list[2] or sort_list[2] == sort_list[0]:
    print("Isosceles")
  else:
    print("Scalene")
