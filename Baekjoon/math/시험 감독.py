import math
n =int(input(""))
A_list = list(map(int,list(input("").split(" "))))
b,c = (input("").split(" "))
cnt = 0
for i in A_list:
    if i-int(b) <= 0:
        cnt+=1
        continue
    else:
        cnt+=1
        i = (i-int(b))/int(c)
        cnt +=math.ceil(i) 
print(cnt)
