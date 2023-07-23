def solution(n):
    # n=1->1,n=2->1,n=3->2,n=4->1,n=5->2,n=6->2,n=7->2,n=8->1,n=9->3
    # 약수 중 홀수?
    cnt = 0
    for i in range(1,n+1):
        if n%i==0 and i%2 != 0:
            cnt+=1
    return cnt
