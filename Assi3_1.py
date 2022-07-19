# ================================================================
# Write a program which accept N numbers from user and store it
# into List. Return addition of all elements from that List
# ================================================================
def addition(n):
    sum=0
    for ino in n:
        sum=sum+ino
    return sum


def main():
    list=[]
    size=int(input("Enter how many numbers you want to insert:"))
    for i in range(size):
        no=int(input("Enter the elements in the list:"))
        list.append(no)
    print(list)
    print("Addition of the elements in the list is:",addition(list))
if __name__=="__main__":
    main()