print("Enter num 1")
num1=input()
print("enter num 2")
num2=input()
try:
    print("The sum of these 2 numbers is",int(num1)+int(num2))
except Exception as e:
    print(e)
    print("this Line is very important")