book_dict = {}

n= int(input())
for i in range(n):
  a = input()
  if a not in book_dict:
    book_dict[a] = 1
  else:
    book_dict[a] +=1
book_list = list(book_dict.items())
book_list.sort(key = lambda x:(-x[1],x[0]))
print(book_list[0][0])
