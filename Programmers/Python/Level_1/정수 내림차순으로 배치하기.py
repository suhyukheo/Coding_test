def solution(n):
    n=list(map(int,str(int(n))))
    n.sort(reverse=True)
    n=''.join(map(str,n))
    return int(n)