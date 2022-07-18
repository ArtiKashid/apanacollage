#''' Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. List
# contains the numbers which are accepted from user. Filter should
# filter out all such numbers which are even. Map function will
# calculate its square. Reduce will return addition of all that numbers."""
#n=int(input("Enter the elements"))

from functools import reduce

nums = []
isize=int(input("Enter the element"))
for i in range(isize):
    no=int(input("Enter the elements in the list"))

    nums.append(no)
evens=list(filter(lambda n:n%2==0,nums))
print("evens",evens)

Square=list(map(lambda n:n*n,evens))
print("Square is",Square)

sum=reduce(lambda a,b:a+b ,Square)

print("sum is",sum)