# ================================================================
# Write a program which accept one number for user and check
# whether number is prime or not
# ================================================================
def PrimeNo(inum):

    if (inum==1):
        return True
    for ino in range(2,inum):
        if (inum%ino)==0:
            # Once the control comes here, i.e the number
            # is not prime (b'cos of, for loop condition)
            # Now, Do not procced forward, break the loop
            # and return False

            break;

    if(ino == (inum-1)):
        return True
    else:
        return False

def main():
    inumber=int(input("Enter the number :"))
    #call the function
    if(PrimeNo(inumber)):
        print("The Number is Prime")
    else:
        print("The number is not prime")
if __name__=="__main__":
    main()