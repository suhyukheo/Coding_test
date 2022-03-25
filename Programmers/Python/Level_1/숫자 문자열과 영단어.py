def solution(s):
    numbers=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(numbers)):
        if numbers[i] in s:
            s=s.replace(numbers[i],str(i))
    return int(s)