def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort(reverse=True)
        if len(rank)>k:
            rank.pop(-1)
        answer.append(rank[-1])
    return answer
