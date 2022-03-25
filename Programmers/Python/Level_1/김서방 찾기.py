def solution(seoul):
    a=[i for i in range(len(seoul)) if seoul[i]=='Kim']
    return '김서방은 '+str(a[0])+'에 있다'