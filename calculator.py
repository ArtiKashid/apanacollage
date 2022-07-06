first=input("Enter First number:")
operator=input("Enter operator(+,-./,*,%):")
second=input("enter second number:")

first=int(first)
second=int(second)

if operator=="+":
    print(first+ second)
elif operator=="-":
    print(first-second)
elif operator=="/":
    print(first/second)
elif operator=="*":
    print(first*second)
elif operator=="%":
    print(first%second)
else:
    print("invalid oeration")