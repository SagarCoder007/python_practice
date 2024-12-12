def factorial(n):
    if n == 0 or n == 1:
      return 1
    else:
     return n * factorial(n-1)
num=int(input("enter a non_negative no :"))
if num<0:
  print("plz enter a non-negative number")

else:
  result=factorial(num)
  print(f"the factoiral of {num} = {result}")
  
