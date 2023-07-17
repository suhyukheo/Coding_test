def solution(k, m, score):
    score = sorted(score)
    answer = 0
    cnt = []
    while len(score) > 0:
        a = score.pop()
        cnt.append(a)
        if len(cnt) == m:
            answer += len(cnt)*cnt[-1]
            cnt = []
    return answer
