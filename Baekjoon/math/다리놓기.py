import math
n = int(input(""))
for i in range(n):
    a,b = input("").split(" ")
    print(math.comb(int(b),int(a)))
