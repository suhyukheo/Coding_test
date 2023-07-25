def solution(X, Y):
    X_count =[0]*10
    Y_count =[0]*10
    answer = []
    ret = ""
    for i in X:
        X_count[int(i)] +=1
    for i in Y:
        Y_count[int(i)] +=1
    for i in range(10):
        if X_count[i] > 0 and Y_count[i] >0 and X_count[i]>Y_count[i]:
            for j in range(Y_count[i]):
                answer.append(i)
        elif X_count[i] > 0 and Y_count[i] >0 and X_count[i]<Y_count[i]:
            for j in range(X_count[i]):
                answer.append(i)
        elif X_count[i] > 0 and Y_count[i] >0 and X_count[i]==Y_count[i]:
            for j in range(X_count[i]):
                answer.append(i)
        else:
            continue
    answer.sort(reverse = True)
    if len(answer) == 0:
        return "-1"
    elif sum(answer) == 0:
        return "0"
    else:
        answer.sort(reverse =True)
        for i in answer:
            ret +=str(i)
        return ret
