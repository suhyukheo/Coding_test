# 총값에 내린사람 빼기 탄사람 더하기 
# 그 중 가장 큰 값 계산하기 예외처리는 신경안써도됨 
p_sum=0
p_max=0
for i in range(10):
  a,b=map(int,input().split(" "))
  p_sum-=a
  p_max=max(p_sum,p_max)
  p_sum+=b
  p_max=max(p_sum,p_max)
print(p_max)
  