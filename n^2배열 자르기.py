def solution(n, left, right):
    array=[]
    for i in range(int(left),int(right+1)):
        d,r=i//n,i%n
        if r<(d+1): 
          array.append(d+1)
        elif r>=(d+1): 
          array.append(r+1)
    return array