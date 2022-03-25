def solution(s):
    s=(s.split())
    s=list(map(int,s))# 인트로 변화 시키지 않으면 -4를 최댓값으로 변환하더라 부호를 신경안쓰나봐..
    result=str(min(s))+" "+str(max(s))
    return result