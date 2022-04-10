def binary_search(start,end,target):
    while True:
        mid=(start+end)//2
        if start>end:
            return False
        if (mid**2)==target:
            return mid
        elif target>(mid**2):
            start=mid
            continue
        elif target<(mid**2):
            end=mid
n=int(input())
print(binary_search(1,n,n))