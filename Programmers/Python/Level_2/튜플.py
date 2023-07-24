def solution(s):
    answer = []
    check_list = [ ]
    check_n= 0
    s = s[1:-1]
    tmp = []
    tmp_s =''
    for i in s:
        if i == '{':
            check_n = 1
        elif i == '}':
            tmp.append(tmp_s)
            check_list.append(tmp)
            tmp_s = ''
            check_n = 0
        elif check_n == 1 and i != ",":
            tmp_s +=i
        elif check_n == 1 and i == ",":
            tmp.append(tmp_s)
            tmp_s = ''
        elif check_n == 0 and i == ',':
            tmp = []
    check_list.sort(key=len)
    for i in check_list: 
        for j in i:
            if j not in answer:
                answer.append(j) 
    answer = list(map(int,answer))
    return answer
