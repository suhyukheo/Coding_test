num_dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
'6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
dict_swap = {v:k for k,v in num_dict.items()}
m,n = map(int, input().split())

answer = []
answer2 = []
for i in range(m,n+1):
   i = str(i)
   tmp = []
   for j in i:
     tmp.append(num_dict[j])
   answer.append( ' '.join(tmp))
   
answer.sort()
for i in answer:
  i = i.split(" ")
  tmp = []
  for j in i:
    tmp.append(dict_swap[j])
  answer2.append(''.join(tmp))

for i in range(len(answer2)):
    if i%10 == 0 and i != 0:
        print(sep="\n")
    print(answer2[i], end=" ")
