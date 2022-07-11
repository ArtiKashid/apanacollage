#Write a program which contains one function that accept one number from user and returns
#true if number is divisible by 5 otherwise return false.

def fun(no):
    if no%5==0:
        print("True")
    else:
        print("False")

def main():
    no=int(input("Enter the number"))
    fun(no)
if __name__=="__main__":
    main()