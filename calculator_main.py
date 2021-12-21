def addition(a,b):
  sum=a+b
  print("The result is : ",sum)
def subt(a,b):
  sub=a-b
  print("The result is : ",sub)
def mult(a,b):
  prod=a*b
  print("The result is : ",prod)
def divide(a,b):
  div=a/b
  print("The result is : ",div)
def expo(a,b):
  exp=a**b
  print("The result is : ",exp)

a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponent")
ch=int(input("Enter your choice : "))
if ch==1:
  addition(a,b)
elif ch==2:
  subt(a,b)
elif ch==3:
  mult(a,b)
elif ch==4:
  divide(a,b)
elif ch==5:
  expo(a,b)
else:
  print("Invalid choice")          
