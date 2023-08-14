n = int(input(""))
answer = 0
for i in range(n):
    a = input("")
    cnt = []
    chk = False
    for i in a:
        if i in cnt and cnt[-1] != i:
            chk = True
            break
        else:
            cnt.append(i)
    if chk == False:
        answer+=1
print(answer)
