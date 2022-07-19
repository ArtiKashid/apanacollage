# ================================================================
# Write a program which accept N numbers from user and store it
# into List. Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number
# to ChkPrime() function which is part of our user defined module
# named as MarvellousNum. Name of the function from main python
# file should be ListPrime().
# ================================================================
import Module_prime as M
def listprime(list):
    isum=0
    for iNum in list:
        if(M.ChkPrime(iNum)):
            isum=isum+iNum
    return isum
def main():
    list=[]
    size=int(input("Enter size of list:"))
    for i in range(size):
        no=int(input("Enter elements in the list:"))
        list.append(no)
    print(list)
    iret= listprime(list)
    print("The addition of all prime number is : ",iret)


if __name__=="__main__":
    main()