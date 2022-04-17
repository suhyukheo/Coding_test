def solution(n, arr1, arr2):
    result=[]
    for i,j in zip(arr1, arr2):
        a12=str(bin(i|j)[2:]) # 1,or 0 이니까 비트연산자를 사용해도 되는 조건이 맞아 떨어짐
        a12=a12.zfill(n) #n의 자릿수 만큼 앞에 0을 채워주는 함수 이 외에도 rjust('n','i') ,ljust('n','i') 처럼 앞뒤에 
        # 왼쪽이나 오른쪽에 원하는 숫자를 자릿수 만큼 채워주는 것도 가능 
        a12=a12.replace('1','#')# replace함수를 이용해서 원하는 문자를 바꿔준다.
        a12=a12.replace('0',' ')
        result.append(a12)
    return result