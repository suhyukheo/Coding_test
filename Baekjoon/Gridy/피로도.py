A,B,C,M=map(int,input().split(" "))
work=0
p=0
if A>M:#예외
  print(0)
else:
  for i in range(24):
    if p+A<=M:
      p+=A
      work+=B
    else:
      if p-C>=0:
        p-=C
      else:
        p=0
  print(work)
    