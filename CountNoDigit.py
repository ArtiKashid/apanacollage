##################################################################
#
#Write a Python Program to Count the Number of Digits in a Number?

#################################################################
n=int(input("Enter number:-"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The total number of digits are:",count)

