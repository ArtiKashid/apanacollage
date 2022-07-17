##############################################################################

#Write a Python Program to Check if a Number is a Perfect Number
#-> perfect number, a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#  Other perfect numbers are 28, 496, and 8,128.

##############################################################################
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is  Perfect number!")
else:
    print("The number is not a Perfect number!")