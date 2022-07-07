# Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5
# Output : 16

def add(no1, no2):
    add = no1 + no2
    return add


def main():
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    print("Addition is :" ,x + y)


if __name__ == "__main__":
        main()