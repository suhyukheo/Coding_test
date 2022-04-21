# 테스트 케이스를 T번 받는다. 배열을 받는다 무조건 10자리고 거기서 3번째로 큰수를 뽑을거다.
t=int(input())
result=[]
for i in range(t):
  a=list(map(int,input().split(" ")))
  a.sort()
  result.append(a[-3])
for i in range(t):
  print(result[i])
  