n=int(input())
nums=list(map(int,input().split(" ")))
result=sorted(nums)
print(result[0],result[-1])