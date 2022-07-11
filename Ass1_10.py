#6.Write a program which accept number from user and check whether that number is positive or
#negative or zero.
#Input : 11    Output : Positive Number
#Input : -8    Output : Negative Number
#Input : 0    Output : Zero

def ChkNum(no):
    if no>0:
        print("Number is Positive")
    elif no<0:
        print("Number is Negative")
    elif no==0:
        print("Number is Zero")
def main():
    no1=int(input("Please Enter the number"))
    ChkNum(no1)
if __name__=="__main__":

    main()