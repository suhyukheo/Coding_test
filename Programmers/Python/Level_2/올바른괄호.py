def solution(s):
    stack=list(s)
    point = 0 
    if s[0] == ')' or len(s)%2!=0:
        return False 
    else:
        while len(stack) >= 3:
            a = stack.pop(point)
            b = stack.pop(point)
            if a == '(' and b ==')':
                if point > 0:
                    point -= 1
                continue
            else:
                stack.insert(point,b)
                stack.insert(point,a)
                point +=1
    if len(stack)%2 == 0:
        if len(stack) ==0:
            return True
        else:
            a = stack.pop(0)
            b = stack.pop(0)
            if a == '(' and b==')':
                return True
            else:
                return False
    else:
        return False 
