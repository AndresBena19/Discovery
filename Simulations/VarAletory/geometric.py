#!/usr/bin/python

import math

def fullP(p,n):
 full=[]
 m=11
 pe=0

 for a in range(p,n):
  p=1
  x=a

  while(x!=1):
    p=p+1
    x=(a*x)%m

  if(p==m-1):
   r=(a/float(10))
   a=0
   p=0.8
   cont=0.0

   cont=a+round((math.log(1.0-r)/math.log(p)),1)
   print "Geometric:" + str(cont)





if __name__ == "__main__":

    fullP(1,9)

