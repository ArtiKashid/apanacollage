##############################################################

#Write a Python Program to Check if a Number is a Prime Number?

##############################################################
n=int(input("Enter the numner:"))
if n > 1:

    for i in range(2,n):
        if (n % i==0):
            print("Number is  not prime")
        else:
            print("number is  prime")
        break

