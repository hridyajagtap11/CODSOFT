print("***** Calculator *****")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
choice=int(input("Enter your choice:"))
num1=int(input("Enter value of num1:"))
num2=int(input("Enter value of num2:"))
if(choice==1):
    sum=num1+num2
    print("Addition of two numbers is",sum)
elif(choice==2):
    subtract=num1-num2    
    print("Subtraction of two numbers is",subtract)
elif(choice==3):
    multiply=num1*num2
    print("Multiplication of two numbers is",multiply)
elif(choice==4):
    divide=float(num1)/float(num2)
    print("Division of two numbers is",divide)
elif(choice==5):
    modulus=num1%num2
    print("Modulus of two numbers is",modulus)    
else:
    print("INVALID OPTION")            