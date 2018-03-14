a=int(input())
b=int(input())
if num in range(a,b+1):
  for i in range (2,num):
    while (num%i)!=0:
      print(num)
      break
