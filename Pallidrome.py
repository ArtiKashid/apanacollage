#####################################################################
#
##Write a Python Program to Check if a Number is a Palindrome or not?
#eg->121 is pallidrome
######################################################################
n=int(input("Enter the number:"))
rev=0
temp=n
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is pallidrome!")
else:
    print("The number is not pallidrome!")


