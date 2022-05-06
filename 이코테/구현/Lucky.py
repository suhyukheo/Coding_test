n=list(map(int,input()))
n_=int(len(n)/2)
if sum(n[0:n_]) ==sum( n[n_:]):
    print('LUCKY')
else:
  print('READY')