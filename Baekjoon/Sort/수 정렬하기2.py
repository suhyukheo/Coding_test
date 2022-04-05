n=int(input())
nums=list(map(int,input().split()))
nums.sort()
for i in range(n):
    print(nums[i])