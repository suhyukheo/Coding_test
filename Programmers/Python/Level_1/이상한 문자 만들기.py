def solution(s):
    s=list(s)
    count=0
    for i in range(len(s)):
        if s[i]==" ":
            count=0
            continue
        else:
            if count%2==0:
                s[i]=chr(ord(s[i])-32)
                count+=1
            else:
                count+=1
    return "".join(s)