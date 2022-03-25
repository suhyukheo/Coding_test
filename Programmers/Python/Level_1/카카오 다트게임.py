def solution(dR):
    result=[]
    num="0123456789"
    SDT="SDT"
    imt="*#"
    dR=dR.replace("10","A")
    for i in dR:
        if i in num:
            result.append(int(i))
            continue
        elif i =="A":
            result.append(10)
            continue
        elif i in SDT:
            if i=="S":
                n=result.pop()
                result.append(n**1)
                continue
            if i=="D":
                n=result.pop()
                result.append(n**2)
                continue
            if i=="T":
                n=result.pop()
                result.append(n**3)
                continue
        elif i in imt:
            if i=="*":
                n=result.pop()
                if len(result)>=1:
                    result[-1]*=2
                result.append(n*2)    
                continue
            elif i=="#":
                n=result.pop()
                result.append(n*-1)
                continue
                
            
    return sum(result)
