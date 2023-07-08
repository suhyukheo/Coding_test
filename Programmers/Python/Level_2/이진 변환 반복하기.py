def check_num(s):
    if s == '1':
        return True
    return False

def solution(s):
    answer = [0,0]
    while 1:
        if check_num(s):
            break
        else:
            count = 0
            ret = ""
            for i in s:
                if i == '0':
                    count +=1
                else:
                    ret +=i
            answer[0]+=1
            answer[1]+=count
            answer_len = len(ret)
            s = bin(answer_len)[2:]
    return answer
