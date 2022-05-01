# 현재값(for(1,len(s))에 넣어서 진행) 또는 전체값(s[0]값 넣어서 )이 1보다 작으면 더하기 연산을 아니면 곱하기 연산을 진행
s=list(map(int,input()))
result=s[0]
for i in range(1,len(s)):
  if s[i]<=1 or result<=1:
    result+=s[i]
  else:
    result*=s[i]
print(result)

    