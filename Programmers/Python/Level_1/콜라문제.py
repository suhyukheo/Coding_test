def solution(a, b, n):
    bottle_cnt = 0
    while n >= a:
        bottle = int(n/a)
        bottle_d =int(n%a)
        n = (b*bottle)+bottle_d
        bottle_cnt += b*bottle
    return bottle_cnt
