n,m=map(int,input().split())
line=[ int(input()) for i in range(n)]
line.sort()
def binary_search(start,end,target):
  while True:
    mid=(start+end)//2
    sum_=0
    if start>end:
      return False
    for i in line:
      sum_+=i//mid
    if sum_==target:
      return mid
    if sum_>target:
      start=mid+1
    elif sum_<target:
      end=mid-1
print(binary_search(1,line[-1],m))
      
      