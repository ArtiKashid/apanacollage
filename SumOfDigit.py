#####################################################################

#Write a program to find the sum of the digits of a number in Python?

#####################################################################
n=int(input("Enter the number:->"))
sum=0
while(n>0):
    num=n%10
    sum=sum+num
    n=n//10
    print("Sum of digit is",sum)

