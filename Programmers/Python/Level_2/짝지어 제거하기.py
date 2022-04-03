def solution(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i) 
            continue
        elif stack[-1]==i: 
            stack.pop() 
            continue
        else: 
            stack.append(i)
    if len(stack)==0:
        return 1
    else:
        return 0