#법칙 -> 공포도가 X 인 사람은 X명이상의 그룹으로 
n=int(input())
a=list(map(int,input().split(" ")))
a.sort()
cnt=0
result=0
# while len(a)>0: 이렇게 풀면 안되나..
#   b=a[-1]
#   cnt+=1
#   for i in range(b):
#     a.pop()
#     if len(a)==0:
#       break
# print(cnt)