m=int(input())
n=int(input())
result = []
for num in range(m,n+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            result.append(num)  # error가 없으면 소수리스트에 추가
            
if len(result) > 0 :
    print(sum(result))
    print(min(result))
else:
    print(-1)