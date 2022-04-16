a=int(input())
divisor=list(map(int,input().split(" ")))
divisor.sort()
print(divisor[-1]*divisor[0])