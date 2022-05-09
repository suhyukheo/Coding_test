a=list(input())
num=[]
alpha=[]
for i in a:
  if 'A'<=i<='Z':
    alpha.append(i)
  else:
    num.append(i)
alpha.sort()
num=list(map(int,num))
alpha.append(str(sum(num)))# 숫자 더한거 리스트에 추가 해줄때 문자형으로 변환 안해줘서 expected str instance, int found 에러뜬거
print("".join(alpha))