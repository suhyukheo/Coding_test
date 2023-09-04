def solution(s, skip, index):
    ret =""
    skip =list(skip)
    for i in s:
        x = 1
        b = index
        while x <= b:
            a = chr((ord(i)+x))
            if ord(a) > 122:
                a = chr(ord(a)-26)
            if a in skip:
                b +=1
            x+=1
            print(a)
        ret +=a
            
    return ret 
