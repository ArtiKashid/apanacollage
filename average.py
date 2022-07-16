#########################################################################
# #Program to find the average of numbers in a list in Python


#########################################################################
n=int(input("Enter how many numbers to be entered in the list:->"))
a=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    a.append(element)###by using append method we can add new element at last
    #print(a)
    avg=sum(a)/n
    print("Average of element is:",round(avg,2))  ##round(avg,2) rounds the average upto 2 decimal places.



