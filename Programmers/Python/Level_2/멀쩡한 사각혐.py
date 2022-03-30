import math
def solution(w,h):
    gcd_=math.gcd(w,h)
    return w*h-((w/gcd_)+(h/gcd_)-1)*gcd_