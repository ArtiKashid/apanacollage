 #Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.
#Input : 11 5
#Output : 16
def add(n1,n2):
    add=n1+n2
def main():
    no1=int(input("Enter first number"))
    no2=int(input("Enter second number"))
    add=no1+no2
    print("Addition is ",add)
if __name__=="__main__":
     main()