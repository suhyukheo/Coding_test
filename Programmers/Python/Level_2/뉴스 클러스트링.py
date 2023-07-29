def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    answer = 0
    tmp1 = []
    tmp2 = [] 
    for i in range(0,len(str1)-1):
        a = str1[i:i+2]
        if a.isalpha():
            tmp1.append(a)
    for i in range(0,len(str2)-1):
        a = str2[i:i+2]
        if a.isalpha():
            tmp2.append(a)
    union1 = tmp1.copy()
    union2 = tmp1.copy()
    for i in tmp2:
        if i not in union1:
            union2.append(i)
        else:
            union1.remove(i)
    inter = []
    for i in tmp2:
        if i in tmp1:
            tmp1.remove(i)
            inter.append(i)
    if len(union2) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter)/len(union2)*65536)
    
    
    
