n = int(input())
for i in range(n):
  cnt = 0.000
  arr = input().split(" ")
  arr = list(map(int,arr))
  avr = sum(arr[1:])/arr[0]
  for i in arr[1:]:
    if i > avr:
      cnt +=1
  print(f"{(cnt/arr[0])*100:.3f}%")
