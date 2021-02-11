i=input
for _ in'_'*int(i()):
 n,m=map(int,i().split());s=0
 for a in range(1,n):
  for b in range(a+1,n):
   if(a*a+b*b+m)//(a*b)==(a*a+b*b+m)/(a*b):s+=1
 print(s)