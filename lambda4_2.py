# Write a program which contains one lambda function which accepts
# two parameters and return its multiplication
# ==============================================================
#mult = Lambda no1,no2: (no1 * no2)
Mult = lambda iNo1, iNo2 : (iNo1 * iNo2)

def fun(n1,n2):
    iret=Mult(n1,n2)
    return iret
def main():
    val1=int(input("Enter the first number:"))
    val2=int(input("Enter the Second number:"))

    print("Multiplication of number is",fun(val1,val2))
if __name__=="__main__":
    main()
