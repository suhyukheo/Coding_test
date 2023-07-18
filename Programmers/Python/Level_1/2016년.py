def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    weeks = ['FRI',"SAT",'SUN','MON',"TUE",'WED','THU']
    if a == 1:
        return weeks[(b%7)-1]
    else:
        temp = 0 
        for i in range(a-1):
            temp += days[i]
        return weeks[((temp+b)%7)-1]
