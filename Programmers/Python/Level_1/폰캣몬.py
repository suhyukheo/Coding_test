def solution(nums):
    n=len(nums)//2
    nums=set(nums)
    nums=list(nums)
    if n<=len(nums):
        return n
    else:
        return len(nums)