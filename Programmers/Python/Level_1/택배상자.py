def solution(order):
    answer = 0
    i = 1
    container = []
    while i < len(order)+1:
        container.append(i)
        while container and container[-1] == order[answer]:
            answer += 1
            container.pop()
        i += 1
            
    return answer
