n_list = list(map(int,list(input(""))))
n_list.sort(reverse=True)
n_list = list(map(str,n_list))
print("".join(n_list))
