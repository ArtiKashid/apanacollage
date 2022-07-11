# ================================================================
# Write a program which contains one lambda function which accepts
# one parameter and return power of two
# ================================================================
def Powtwo(no):

    x=lambda no:(no*no)
    return x(no)

def main():
    ivalue=int(input("Enter the number"))

    iret= Powtwo(ivalue)
    print("the power of two of given number is",iret)
if __name__=="__main__":
    main()