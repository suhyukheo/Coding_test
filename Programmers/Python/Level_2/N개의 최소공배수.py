import math 
def solution(arr):
    arr_lcm=arr[0]
    for i in range(1,len(arr)):
        arr_lcm=arr_lcm*arr[i]//math.gcd(arr_lcm,arr[i])
    return arr_lcm
