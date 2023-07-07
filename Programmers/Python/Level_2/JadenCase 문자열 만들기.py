def solution(s:str)->str:
    s = s.split(" ")
    answer=[]
    ret = ""
    for i in s:
        if i!=" " and i[0].isalpha():
            answer.append(i[0:1].upper() + i[1:].lower())
        else:
            answer.append(i.lower())
    for i in answer:
        if i == "":
            ret+=" "
        else: 
            ret+=i+" "
    return ret[:-1]
