def solution(numbers):
    result=list(map(str,numbers))
    result.sort(key=lambda x:x*3,reverse=True)
    result="".join(result)
    return str(int(result))
#1.순열을 통한 접근 --> 시간초과
#2.자릿수 별로 판단하기 기술적인 문제가 있었으나 어지저찌 찾아냄 11번이 틀림
#3.테스트케이스의 0000이 있을 수 있겠내..--> 4번에 미리 문자열을 묶고 int에 한번 넣어서 0000인 경우 0으로 바꿔준다.