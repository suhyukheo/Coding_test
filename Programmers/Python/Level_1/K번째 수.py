def solution(array, commands):
    result=[]
    for a in commands:
        i,j,k=a
        new=array[i-1:j]
        new.sort()
        result.append(new[k-1])

        

    return result
