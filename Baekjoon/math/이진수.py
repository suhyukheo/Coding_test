# 숫자를 입력받자.
# 숫자를 이진수로 만들어보자
# 숫자를 리스트에 담아서 역순정렬 해보자 
# 1인숫자의 자릿수를 담아 보자. 
# 더 나은 방법을 찾아보자

t=int(input())
for i in range(t):
  b=int(input())
  b=list((bin(b)[2:]))
  b.reverse()
  for i in range(len(b)):
    if b[i]=='1':
      print(i,end=" ")

