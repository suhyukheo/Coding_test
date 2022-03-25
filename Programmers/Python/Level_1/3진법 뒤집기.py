def solution(n):
    result=''
    while n>0:
        q,r= divmod(n,3)
        n=q
        result+=str(r)   
    return  int(result,3)
