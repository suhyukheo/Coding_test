n = int(input(""))
n_list = []
for i in range(n):
    a = int(input(""))   
    n_list.append(a)
n_list.sort(reverse = True)
for i in n_list:
    print(i)
